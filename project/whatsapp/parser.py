from .model import IncomingMessage

async def parsed_message(data:dict) -> IncomingMessage:
    
                 
    return IncomingMessage(sender_id = data["From"],
                           message_id = data["MessageSid"],
                           text = data["Body"])