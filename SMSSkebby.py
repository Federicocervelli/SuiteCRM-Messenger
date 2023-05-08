# pip install requests
import requests
import json
import sys
import datetime

BASEURL = "https://api.skebby.it/API/v1.0/REST/"

#qualita del messaggio
MESSAGE_HIGH_QUALITY = "GP"
MESSAGE_MEDIUM_QUALITY = "TI"
MESSAGE_LOW_QUALITY = "SI"


def json_serial(obj):
    #serializzazione in formato json dell'oggetto inviaSMS per trasmetterlo tramite richiesta HTTP POST all'API

    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

    raise TypeError ("Type not serializable")


def login(username, password):
    #ritorna una coppia (user_key, session_key) dopo l'autenticazione

    r = requests.get("%slogin?username=%s&password=%s"
                     % (BASEURL, username, password))

    if r.status_code != 200:
        print("--Errore : Impossibile effettuare il Login--")
        return None

    user_key, session_key = r.text.split(';')
    print("--Autenticazione effettuata : Login riuscito--")
    return user_key, session_key


def sendSMS(auth, sendsms):

    headers = { 'user_key': auth[0],
                'Session_key': auth[1],
                'Content-type' : 'application/json' }

    #json.dumps() converte l'oggetto sendsms in stringa json prima di includerlo nella richiesta HTTP POST
    r = requests.post("%ssms" % BASEURL,
                      headers=headers,
                      data=json.dumps(sendsms, default=json_serial))

    if r.status_code != 201:
        print(r.text)
        return None

    #converte la stringa json in oggetto python
    return json.loads(r.text)


if __name__ == "__main__":
    f = open('chiavi.json')
    credenziali = json.load(f)
    auth = login(credenziali['email'], credenziali['password'])

    if not auth:
        print("Unable to login..")
        sys.exit(-1)

    sentSMS = sendSMS(auth,
                      {
                          "message" : "Messaggio di prova",
                          "message_type" : MESSAGE_HIGH_QUALITY,
                          "returnCredits" : False,
                          "recipient": ["+393318389305",],

                          # Place here a custom sender if desired
                          "sender": None,

                          # Postpone the SMS sending by 5 minutes
                          "scheduled_delivery_time" : None
                      })

    if sentSMS['result'] == "OK":
        print("--Messaggio inviato correttamente--")
    f.close()
