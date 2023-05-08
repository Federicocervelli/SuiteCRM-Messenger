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
    #Recupero messaggi non inviati dall'API
    messaggi = collezione(id)
    
          
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
        return -1
        
    print("Loggato correttamente con id sessione: " + id)
    logging.debug("Conclusa funzione autenticazione, l'id sessione è: " + id)
    return id
   
def collezione(id):
    dataurl = """https://testkeyall.cittadigitale.org/service/v4/rest.php?method=get_entry_list&input_type=JSON&response_type=JSON&rest_data={
                    "session":\""""+ id + """\",
                    "module_name":"os_Notifiche_comunicazioni",
                    "query":"is_sent = 0",
                    "order_by":"",
                    "offset":0,
                    "select_fields":[],
                    "link_name_to_fields_array":{},
                    "max_result":10,
                    "deleted":0
                }
            """    
    payload = {}
    headers = {}
    
    try:
        response = requests.request("GET", dataurl, headers=headers, data=payload)
        
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
        resultCount = jsonResponse["result_count"]
        totalCount = jsonResponse["total_count"]
        
    except KeyError:
        logging.error(f'errore nella collezione: ' + response.text)
        print(f'errore nella collezione: ' + response.text)
        return -1
        
    print("Collezionati correttamente " + str(resultCount) + " su " + str(totalCount) + " messaggi non anccora mandati totali.")
    logging.info("Collezionati correttamente " + str(resultCount) + " su " + str(totalCount) + " messaggi non anccora mandati totali.")
    return jsonResponse
    
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