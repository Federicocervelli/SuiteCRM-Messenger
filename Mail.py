from email.message import EmailMessage
#tecnologia standard per mantenere una connessione internet sicura per tenere riservati i dati sensibili
import ssl
#per mandare la mail
import smtplib

#nel progetto inseriremo invece i campi del file json quindi item[i].email_mittente.as_string
email_sender = 'lorenzoronconi60@gmail.com'
email_password = 'ysdchqchxfobolvd'
email_receiver = 'lorenzo.ronconi@osmosit.com'
subject = 'Test'
body = """"
It works!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

#specifichiamo prima il servizio con la quale spediamo la mail (gmail)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

