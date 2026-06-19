# b2bflow-challenge

Desafio feito em Python, onde é preciso ler contatos vindos do Supabase e enviar uma mensagem pra eles, via Z-API.

## Requisitos

Criar conta em `https://supabase.com`
Criar conta em `https://app.z-api.io`

## Setup da tabela (Supabase)

No SQL Editor do Supabase, rode:

\`\`\`sql
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
\`\`\`

E depois insira de pelo menos 1 contato, com o telefone no formato 55DDDNUMERO (ex: `5571912345678`).

## Criação da instância (Z-API)

Após criar sua conta no Z-API, escaneie o QR Code com o seu WhatsApp, isso criará uma instância.

## Variáveis de ambiente

Crie um arquivo `.env` na raiz com base no `.env.example`:

\`\`\`
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
\`\`\`

- `SUPABASE_URL`: Encontrado em Project Overview, logo abaixo do nome do projeto
- `SUPABASE_KEY`: Encontrado em Project Settings -> API Keys (buscar anon public)
- `ZAPI_INSTANCE_ID` e `ZAPI_TOKEN`: São encontrados no painel, assim criar sua instância na Z-API

## Como rodar

\`\`\`bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
\`\`\`

## Tecnologias

- Python
- Supabase
- Z-API