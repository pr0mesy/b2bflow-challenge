from supabase import create_client
from app.config import SUPABASE_KEY, SUPABASE_URL

client = create_client(SUPABASE_URL, SUPABASE_KEY)

# essa funcao executa uma query simples: buscar todos
# os contatos na minha tabela de contatos
def get_contacts():
    response = client.table("contacts").select("*").execute()
    return response.data