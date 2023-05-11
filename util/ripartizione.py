import json
import asyncio
import util.sms
import util.mail
import logging
logger = logging.getLogger(__name__)

async def ripartizione(data):
    messages = data['entry_list']

    tasks = []
    for msg in messages:
        task = asyncio.create_task(sendMsg(msg))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

async def sendMsg(msg):
    if msg['name_value_list']['notification_type']['value'] == 'EMAIL':
        print("mail")
        await util.mail.main()
    elif msg['name_value_list']['notification_type']['value'] == 'SMS':
        print("sms")
        await util.sms.main()
    else:
        print("errore")
        logging.error("Errore invio messaggio ")

def main(data):
    asyncio.run(ripartizione(data))
    
