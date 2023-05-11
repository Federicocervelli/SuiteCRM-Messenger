import json
import asyncio
from SMSSkebby import main as SMS
from Mail import main as EMAIL

async def ripartizione(json_data):
    for messaggio in json_data['entry_list'].items():
        if messaggio['notification_type']['value'] == 'EMAIL':
            await EMAIL()
        elif messaggio['notification_type']['value'] == 'SMS':
            await SMS()
