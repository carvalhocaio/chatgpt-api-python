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
except AuthenticationError:
    print("Erro de autenticacao: verifique sua OPENAI_API_KEY.")
except RateLimitError:
    print("Limite de taxa excedido: aguarde e tente novamente.")
except (APIConnectionError, APIError):
    print("Erro de rede/servidor ao chamar a API. Tente novamente.")
except BadRequestError as exc:
    print(f"Requisicao invalida: {exc}")
except Exception as exc:
    print(f"Erro inesperado: {exc}")
else:
    code_result = code_response.output_parsed
    print(f"Function Name: {code_result.function_name}")
    print("\nCode:")
    print(code_result.code)
    print(f"\nExplanation: {code_result.explanation}")
    print(f"\nExample Usage:\n{code_result.example_usage}")
