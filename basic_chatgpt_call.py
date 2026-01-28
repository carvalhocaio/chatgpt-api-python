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
        input="Conte uma piada sobre programação em Python",
    )
except AuthenticationError:
    print("Erro de autenticação: verifique sua OPENAI_API_KEY.")
except RateLimitError:
    print("Limite de taxa excedido: aguarde e tente novamente.")
except BadRequestError as exc:
    print(f"Requisicao inválida: {exc}")
except APIConnectionError:
    print("Erro de rede ao chamar a API. Tente novamente.")
except APIError:
    print("Erro do servidor da API. Tente novamente.")
except Exception as exc:
    print(f"Erro inesperado: {exc}")
else:
    print(f"Piada:\n{text_response.output_text}")
