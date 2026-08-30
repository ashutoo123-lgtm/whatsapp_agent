from pydantic import BaseModel
class IncomingMessage(BaseModel):
    sender_id : str
    message_id :str
    text : str