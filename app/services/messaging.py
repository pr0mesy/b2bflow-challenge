from app.integrations.supabase import get_contacts
from app.integrations.zapi import send_message
from app.logger import logger

def send_messages_to_contacts():
    contacts = get_contacts()
    
    for contact in contacts:
        name = contact["name"]
        phone = contact["phone"]
        message = f"Olá, {name} tudo bem com você?"
        
        send_message(phone, message)
        logger.info(f"Mensagem enviada para {name}")