import requests
from app.config import ZAPI_INSTANCE_ID, ZAPI_TOKEN
from app.logger import logger

def send_message(phone: str, message: str):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    
    payload = {
        "phone": phone,
        "message": message
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem: {e}")
        return None