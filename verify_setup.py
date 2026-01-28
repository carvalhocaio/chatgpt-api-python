from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
print("Cliente OpenAI criado com sucesso!")
if not client.api_key:
    raise RuntimeError("OPENAI_API_KEY nao definida. Adicione ao .env ou ao ambiente.")
print("OPENAI_API_KEY carregada: sim")
