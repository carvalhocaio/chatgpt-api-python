from dotenv import load_dotenv
from openai import OpenAI
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


rate_limiter.acquire()
code_response = client.responses.parse(
    model="gpt-5",
    input=[
        {
            "role": "developer",
            "content": (
                "You are a coding assistant. Generate clean,"
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

code_result = code_response.output_parsed

print(f"Function Name: {code_result.function_name}")
print("\nCode:")
print(code_result.code)
print(f"\nExplanation: {code_result.explanation}")
print(f"\nExample Usage:\n{code_result.example_usage}")
