from supabase import create_client
from app.config import SUPABASE_KEY, SUPABASE_URL
from app.models.contact import Contact

client = create_client(SUPABASE_URL, SUPABASE_KEY)

# essa funcao executa uma query simples: buscar todos
# os contatos na minha tabela de contatos
def get_contacts():
    response = client.table("contacts").select("*").execute()
    # optei por usar list comprehension so pra impressionar rs, mas
    # consiste num for que constrói uma lista nova
    return [Contact(name=c["name"], phone=c["phone"]) for c in response.data]