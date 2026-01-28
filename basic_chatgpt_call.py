from dotenv import load_dotenv
from openai import OpenAI

from rate_limiter import RateLimiter

load_dotenv()

client = OpenAI()
rate_limiter = RateLimiter(max_requests=60, per_seconds=60)
rate_limiter.acquire()
text_response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Tell me a joke about Python programming",
)

print(f"Joke:\n{text_response.output_text}")
