from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    BadRequestError,
    OpenAI,
    RateLimitError,
)
from pydantic import BaseModel

from rate_limiter import RateLimiter

load_dotenv()

client = OpenAI()
rate_limiter = RateLimiter(max_requests=60, per_seconds=60)


class CodeOutput(BaseModel):
    function_name: str
    code: str
    explanation: str
    example_usage: str


try:
    rate_limiter.acquire()
    code_response = client.responses.parse(
        model="gpt-5",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are a programming assistant. Generate clean, "
                    "well-documented Python code."
                ),
            },
            {
                "role": "user",
                "content": "Write a simple Python function to add two numbers.",
            },
        ],
        text_format=CodeOutput,
    )
except AuthenticationError:
    print("Authentication error: check your OPENAI_API_KEY.")
except RateLimitError:
    print("Rate limit exceeded: wait and try again.")
except BadRequestError as exc:
    print(f"Invalid request: {exc}")
except (APIConnectionError, APIError):
    print("Network/server error calling the API. Try again.")
except Exception as exc:
    print(f"Unexpected error: {exc}")
else:
    code_result = code_response.output_parsed
    if code_result is None:
        print("The response could not be converted to the expected format.")
    else:
        print(f"Function name: {code_result.function_name}")
        print("\nCode:")
        print(code_result.code)
        print(f"\nExplanation: {code_result.explanation}")
        print(f"\nUsage example:\n{code_result.example_usage}")
