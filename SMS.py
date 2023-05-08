from twilio.rest import Client
from keys import *

client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Test",
    from_ = twilio_number,
    to = my_phone_number
)
