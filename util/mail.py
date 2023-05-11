from email.message import EmailMessage
#tecnologia standard per mantenere una connessione internet sicura per tenere riservati i dati sensibili
import ssl
#per mandare la mail
import smtplib
import logging
import json

logger = logging.getLogger(__name__)


context = ssl.create_default_context()


#specifichiamo prima il servizio con la quale spediamo la mail (gmail)



def invia_mail(mittente, destinatario, oggetto, descrizione, password):
    em = EmailMessage()
    em['From'] = mittente
    em['To'] = destinatario
    em['Subject'] = oggetto
    em.set_content(descrizione)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mittente, password)
        smtp.sendmail(mittente, destinatario, em.as_string())


async def main():
    with open("chiaviMail.json", encoding="UTF-8") as f:
        credenzialiMail = json.load(f)
    invia_mail(credenzialiMail['email_sender'], 'zeke0097@gmail.com', 'Prova', """Ciao Marco""", credenzialiMail['email_password'])
    f.close()
