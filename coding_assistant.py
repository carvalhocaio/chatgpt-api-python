from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    BadRequestError,
    OpenAI,
    RateLimitError,
)
from openai.types.responses import ResponseInputItemParam

from rate_limiter import RateLimiter

load_dotenv()

client = OpenAI()
rate_limiter = RateLimiter(max_requests=60, per_seconds=60)

max_history = 12
messages: list[ResponseInputItemParam] = [
    {
        "role": "developer",
        "content": (
            "You are a Python programming assistant. "
            "Only accept questions related to Python."
        ),
    }
]

while True:
    user_input = input("How can I help? (type 'exit' to quit) ").strip()
    if not user_input:
        continue
    if user_input.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_input})
    if len(messages) > max_history + 1:
        messages = [messages[0], *messages[-max_history:]]

    try:
        rate_limiter.acquire()
        code_response = client.responses.create(
            model="gpt-3.5-turbo",
            input=messages,
        )
    except AuthenticationError:
        print("Authentication error: check your OPENAI_API_KEY.")
        break
    except RateLimitError:
        print("Rate limit exceeded: wait and try again.")
        continue
    except BadRequestError as exc:
        print(f"Invalid request: {exc}")
        continue
    except APIConnectionError:
        print("Network error calling the API. Try again.")
        continue
    except APIError:
        print("API server error. Try again.")
        continue
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        continue
    else:
        response = code_response.output_text or ""
        messages.append({"role": "assistant", "content": response})
        print(f"\n{response}")
