### Installazione Dipendenze

1 - Installare python e controllare che il comando 'pip' funzioni. 
(Potrebbe essere necessario riavviare il terminale dopo l'installazione)

2 - Aprire un terminale sulla cartella del progetto (../SuiteCRM-Messenger), eseguire il seguente comando:
pip install -r .\requirements.txt

### Configurazione Dati

#### Usando il file 'impostazioni.json', inserire le informazioni necessarie al funzionamento del programma.

**verbose** : "true" o "false"  
indica se l'output nei log debba essere piu' dettagliato, per motivi di debugging

**log-path** : "" o "path-ralativo/nomefile.estenzione" o "path-assoluto/nomefile.estensione"  
indica dove deve essere salvato il file di log.

**max-results** : numero  
Numero di risultati che il programma ottiene dal CRM ad ogni ciclo di esecuzione.

**api_url** : "URL"
Url dell'API di suitecrm.
Esempio: "https://testkeyall.cittadigitale.org/service/v4/rest.php"

**email_sender** : "email"  
Email da cui inviare i messaggi.

**email_password** : "password"  
Password API della mail da cui mandare i messaggi.

**skebby_email** : "email"  
Email di Skebby da usare per mandare gli SMS   

**skebby_password** : "password"  
Password dell'account Skebby

### Esecuzione Programma

Per eseguire il programma, aprire il terminale sulla cartella del progetto (../SuiteCRM-Messenger)
ed eseguire il seguente comando: 

python3 inviaMessaggi.py (-v) (logpath)

**-v** : Indica se abilitare il verbose. in caso la flag non sia presente, il programma sceglie di default l'opzione nelle impostazioni.json.

**logpath** Stessa cosa: qui si puo' scegliere un path alternativo per i log, ma se non e' specificato, il programma sceglie di default quello definito in impostazioni.json.