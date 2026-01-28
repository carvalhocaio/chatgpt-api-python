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

max_historico = 12
mensagens: list[ResponseInputItemParam] = [
    {
        "role": "developer",
        "content": (
            "Você é um assistente de programação Python. "
            "Apenas aceite perguntas relacionadas a Python."
        ),
    }
]

while True:
    user_input = input("Como posso ajudar? (digite 'sair' para encerrar) ").strip()
    if not user_input:
        continue
    if user_input.lower() in {"sair", "exit", "quit"}:
        break

    mensagens.append({"role": "user", "content": user_input})
    if len(mensagens) > max_historico + 1:
        mensagens = [mensagens[0], *mensagens[-max_historico:]]

    try:
        rate_limiter.acquire()
        code_response = client.responses.create(
            model="gpt-3.5-turbo",
            input=mensagens,
        )
    except AuthenticationError:
        print("Erro de autenticação: verifique sua OPENAI_API_KEY.")
        break
    except RateLimitError:
        print("Limite de taxa excedido: aguarde e tente novamente.")
        continue
    except BadRequestError as exc:
        print(f"Requisição inválida: {exc}")
        continue
    except APIConnectionError:
        print("Erro de rede ao chamar a API. Tente novamente.")
        continue
    except APIError:
        print("Erro do servidor da API. Tente novamente.")
        continue
    except Exception as exc:
        print(f"Erro inesperado: {exc}")
        continue
    else:
        resposta = code_response.output_text or ""
        mensagens.append({"role": "assistant", "content": resposta})
        print(f"\n{resposta}")
