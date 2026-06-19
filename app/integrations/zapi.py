import requests
from app.config import ZAPI_INSTANCE_ID, ZAPI_TOKEN

def send_message(phone: str, message: str):
    # encontrei a url base pra envio de msgs na documentacao da z-api
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    
    payload = {
        "phone": phone,
        "message": message
    }
    
    response = requests.post(url, json=payload)
    return response.json()
