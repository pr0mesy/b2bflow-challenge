from app.integrations.supabase import get_contacts
from app.integrations.zapi import send_message

def send_messages_to_contacts():
    contacts = get_contacts()
    
    for contact in contacts:
        name = contact["name"]
        phone = contact["phone"]
        message = f"Olá, {name} tudo bem com você?"
        
        send_message(phone, message)
        print(f"mensagem enviada com sucesso pra {name}")