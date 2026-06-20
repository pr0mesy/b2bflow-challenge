from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

# dicionario contendo as variaveis de ambientes obrigatorias,
# pra depois percorrer e, se não encontrar uma, lançar uma exceção
required = {
    "SUPABASE_URL": SUPABASE_URL,
    "SUPABASE_KEY": SUPABASE_KEY,
    "ZAPI_INSTANCE_ID": ZAPI_INSTANCE_ID,
    "ZAPI_TOKEN": ZAPI_TOKEN
}

for name, value in required.items():
    if not value:
        raise ValueError(f"a variável de ambiente {name} não foi definida")
