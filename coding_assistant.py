from dotenv import load_dotenv
from openai import OpenAI

from rate_limiter import RateLimiter

load_dotenv()

user_input = input("How can I help you? ")
client = OpenAI()
rate_limiter = RateLimiter(max_requests=60, per_seconds=60)

rate_limiter.acquire()
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
