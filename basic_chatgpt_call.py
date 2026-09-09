from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    BadRequestError,
    OpenAI,
    RateLimitError,
)

from rate_limiter import RateLimiter

load_dotenv()

client = OpenAI()
rate_limiter = RateLimiter(max_requests=60, per_seconds=60)

try:
    rate_limiter.acquire()
    text_response = client.responses.create(
        model="gpt-3.5-turbo",
        input="Tell a joke about Python programming",
    )
except AuthenticationError:
    print("Authentication error: check your OPENAI_API_KEY.")
except RateLimitError:
    print("Rate limit exceeded: wait and try again.")
except BadRequestError as exc:
    print(f"Invalid request: {exc}")
except APIConnectionError:
    print("Network error calling the API. Try again.")
except APIError:
    print("API server error. Try again.")
except Exception as exc:
    print(f"Unexpected error: {exc}")
else:
    print(f"Joke:\n{text_response.output_text}")
