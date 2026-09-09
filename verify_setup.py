from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
print("OpenAI client created successfully!")
if not client.api_key:
    raise RuntimeError("OPENAI_API_KEY not set. Add it to .env or the environment.")
print("OPENAI_API_KEY loaded: yes")
