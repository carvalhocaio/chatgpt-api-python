# chatgpt-api-python

Pequenos exemplos de uso do OpenAI SDK em Python.

## Configuracao rapida
1. Crie um arquivo `.env` baseado em `.env.example` e defina `OPENAI_API_KEY`.
2. Instale as dependencias com o seu gerenciador preferido.
3. Rode um dos scripts de exemplo.

## Exemplos
- `basic_chatgpt_call.py`: chamada simples.
- `coding_assistant.py`: assistente interativo.
- `structured_output.py`: saida estruturada com Pydantic.

## Security Considerations
- Always keep your API keys secure. Use environment variables or secure key management services in production applications.
- Never commit API keys to version control, and rotate them regularly if they might have been exposed.
- Consider implementing rate limiting in your applications to prevent unexpected API costs.

## Rate limiting (exemplo)
Veja `rate_limiter.py` para um limitador simples de chamadas por processo.

```python
from rate_limiter import RateLimiter

rate_limiter = RateLimiter(max_requests=60, per_seconds=60)
rate_limiter.acquire()
```
