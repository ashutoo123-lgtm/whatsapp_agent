import os 
from twilio.rest import     Client
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
async def message_sender(recipient:str,
                         text : str):
    message = client.messages.create(from_ = TWILIO_AUTH_TOKEN,
                                     to = recipient,
                                     body = text)
    return message.sid