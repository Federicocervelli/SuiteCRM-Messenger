import invio
import ripartizione
import sys
import logging

#Valori di default
verbose = False
path = "/var/log/inviomessaggi.log"



def main():
    #Analisi delle casistiche della chiamata del comando
    analisiComando()
    #Inizializzazione log
    configurazioneLog()
    #Accesso all'API
    autenticazione()
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
    logging.debug("Conclusa funzione autenticazione")
    
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