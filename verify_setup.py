from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
print("OpenAI client created successfully!")
print(f"Using API key: {client.api_key[:8]}...")
