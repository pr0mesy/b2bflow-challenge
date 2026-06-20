from app.integrations.supabase import get_contacts
from app.integrations.zapi import send_message
from app.logger import logger

def send_messages_to_contacts():
    contacts = get_contacts()

    # usando o objeto contact, temos acesso direto aos atributos name e phone
    for contact in contacts:
        message = f"Olá, {contact.name} tudo bem com você?"

        send_message(contact.phone, message)
        logger.info(f"Mensagem enviada para {contact.name}")