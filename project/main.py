from fastapi import FastAPI, Request,HTTPException
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
load_dotenv()
from .whatsapp.clients import message_sender
from .whatsapp.parser import parsed_message
from .llm import generate_llm_response
# secret_token = os.getenv("webhook-verification-token")
app = FastAPI()
# @app.get("/webhook")
# async def  verify_request(request : Request):
    # params = request.query_params
    # token  = params.get("hub.token")
    # mode = params.get("hub.mode")
    # challenge = params.get("hub.challenge")
    # if token == secret_token and mode =="subscribe" :
    #     return int(challenge)
    # else:
    #     raise HTTPException(status_code = 403 , detail  = "verification failed")



@app.post("/webhook")
async def post_request(request : Request):
    
    form = await request.form()
    message = await parsed_message(form)
    response = await generate_llm_response(message.text)
    message_sender(to = message.sender_id,
                   body = response)
    return{"status": "success"}
