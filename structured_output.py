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
                    "Você é um assistente de programação. Gere código "
                    "Python limpo e bem documentado."
                ),
            },
            {
                "role": "user",
                "content": "Escreva uma função simples em Python para somar dois numeros.",
            },
        ],
        text_format=CodeOutput,
    )
except AuthenticationError:
    print("Erro de autenticação: verifique sua OPENAI_API_KEY.")
except RateLimitError:
    print("Limite de taxa excedido: aguarde e tente novamente.")
except BadRequestError as exc:
    print(f"Requisicao inválida: {exc}")
except (APIConnectionError, APIError):
    print("Erro de rede/servidor ao chamar a API. Tente novamente.")
except Exception as exc:
    print(f"Erro inesperado: {exc}")
else:
    code_result = code_response.output_parsed
    if code_result is None:
        print("A resposta não pôde ser convertida para o formato esperado.")
    else:
        print(f"Nome da função: {code_result.function_name}")
        print("\nCódigo:")
        print(code_result.code)
        print(f"\nExplicação: {code_result.explanation}")
        print(f"\nExemplo de uso:\n{code_result.example_usage}")
