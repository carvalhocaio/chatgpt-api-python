from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

user_input = input("How can I help you? ")
client = OpenAI()

code_response = client.responses.create(
    model="gpt-3.5-turbo",
    input=[
        {
            "role": "developer",
            "content": (
                "You are a Python coding assistant. "
                "Only accept Python-related questions."
            ),
        },
        {
            "role": "user",
            "content": f"{user_input}",
        },
    ],
)

print(f"\n{code_response.output_text}")
