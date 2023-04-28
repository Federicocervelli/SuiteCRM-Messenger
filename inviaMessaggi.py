import invio
import ripartizione
import sys

#Valori di default
verbose = False
path = "/var/log/inviomessaggi.log"

def main():
    #Analisi delle casistiche della chiamata del comando
    analisiComando()
    #Accesso all'API
    autenticazione()
    
        
def analisiComando():
    args = sys.argv[1:]
    global path, verbose #Cambio lo scope a globale
    if len(args) == 2 and args[1] == "-v":
        path = args[0]
        verbose = True
    elif len(args) == 1 and args[0] == "-v":
        verbose = True
    elif len(args) == 1:
        path = args[0]
    else:
        stampaErroreSintassi()

def stampaErroreSintassi():
    print("Perfavore usa la sintassi corretta per eseguire il comando!")
    print("Utilizzo corretto: python3 inviaMessaggi.py [-v] [path]")
    
def autenticazione():
    print()