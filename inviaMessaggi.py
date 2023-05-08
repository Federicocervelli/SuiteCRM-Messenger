import invio
import Mail
import ripartizione
import sys
import logging
import requests
from requests.exceptions import HTTPError

#Valori di default
verbose = False
path = "/var/log/inviomessaggi.log"



def main():
    #Analisi delle casistiche della chiamata del comando
    analisiComando()
    #Inizializzazione log
    configurazioneLog()
    #Accesso all'API
    id = autenticazione()
    #test logging in invio
    invio.test()
          
def analisiComando():
    args = sys.argv[1:]
    global path, verbose #Cambio lo scope a globale
    if len(args) == 2 and args[0] == "-v":
        path = args[1]
        verbose = True
    elif len(args) == 1 and args[0] == "-v":
        verbose = True
    elif len(args) == 1:
        path = args[0]
    elif len(args) == 0:
        return
    else:
        stampaErroreSintassi()

def stampaErroreSintassi():
    print("Perfavore usa la sintassi corretta per eseguire il comando!")
    print("Utilizzo corretto: python3 inviaMessaggi.py [-v] [path]")
    
def autenticazione():
    logging.debug("Iniziata funzione autenticazione")
    loginurl = """https://testkeyall.cittadigitale.org/service/v4/rest.php?method=login&input_type=JSON&response_type=JSON&rest_data={
            \"user_auth\":
                { 
                    \"user_name\":\"restuser\",
                    \"password\":\"16517ba81e199867116bc2b0a2279bbd\"},
                    \"application_name\":\"\",
                    \"name_value_list\":{
                    \"name\":\"notifyonsave\",
                    \"value\":\"true\"}
                }
            """
        
    payload = {}
    headers = {}
    
    try:
        response = requests.request("GET", loginurl, headers=headers, data=payload)
        
    except HTTPError as http_err:
        logging.error(f'errore HTTP nel login: {http_err}')
        print(f'errore HTTP nel login: {http_err}')
        return -1
    
    except Exception as err:
        logging.error(f'errore generico nel login: {err}')
        print(f'errore generico nel login: {err}')
        return -1
    
    jsonResponse = response.json()
    
    try:
        id = jsonResponse["id"]
        
    except KeyError:
        logging.error(f'errore nel login: ' + response.text)
        print(f'errore nel login: ' + response.text)
        
    print("Loggato correttamente con id sessione: " + id)
    logging.debug("Conclusa funzione autenticazione, l'id sessione è: " + id)
    return id
   
def configurazioneLog():
    
    if(verbose):
        tipolog = logging.DEBUG
    else:
        tipolog = logging.INFO
        
    logging.basicConfig(filename=path, level=tipolog,
                    format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')
    logging.info("Programma inizializzato con i seguenti parametri: " + str(sys.argv[1:]))
    
if __name__ == "__main__":
    main()