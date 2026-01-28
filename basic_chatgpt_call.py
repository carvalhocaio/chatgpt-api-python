from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
text_response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Tell me a joke about Python programming",
)

print(f"Joke:\n{text_response.output_text}")
