# chatgpt-api-python

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://platform.openai.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.12%2B-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9)](https://docs.astral.sh/uv/)

Small examples of using the OpenAI SDK in Python.

## Table of Contents

- [Quick setup](#quick-setup)
- [Examples](#examples)
- [Security considerations](#security-considerations)
- [Cost management](#cost-management)
- [Conversation context](#conversation-context)
- [Rate limiting (example)](#rate-limiting-example)
- [Credits and reference](#credits-and-reference)

## Quick setup

1. Create a `.env` file based on `.env.example` and set `OPENAI_API_KEY`.
2. Install the dependencies with your preferred package manager.
3. Run one of the example scripts.

## Examples

| Script | Description |
| --- | --- |
| `basic_chatgpt_call.py` | Simple one-off call to the API. |
| `coding_assistant.py` | Interactive assistant that keeps conversation history. |
| `structured_output.py` | Structured output parsed with Pydantic. |
| `verify_setup.py` | Verifies your OpenAI client and API key are configured correctly. |
| `rate_limiter.py` | A simple per-process rate limiter used by the other scripts. |

## Security considerations

- Keep your API keys safe. Use environment variables or a secrets manager in production.
- Never commit API keys to version control, and rotate them regularly if a leak is suspected.
- Consider implementing rate limiting in your applications to avoid unexpected costs.

## Cost management

- Monitor usage and costs on the OpenAI dashboard.
- Different models have different prices, and cost accumulates based on the number of tokens processed (input and output).
- Weigh the trade-off between model capability and cost for each use case.
- During development, you can use free mock endpoints (such as OpenAI's mock API on Beeceptor) to test the integration at no cost.
- When using third-party mocks, use a dummy key and avoid sending sensitive data.

### API mock (optional)

To point your tests at a mock, set `OPENAI_BASE_URL` in `.env`. The SDK uses this variable automatically.

## Conversation context

- For chatbots, maintain history by including previous messages in `input`.
- Long conversations consume more tokens and increase cost; trim the history as needed.

```python
messages = [
    {"role": "developer", "content": "You are a Python programming assistant."},
]

messages.append({"role": "user", "content": "How do I write a loop in Python?"})
response = client.responses.create(model="gpt-3.5-turbo", input=messages)
messages.append({"role": "assistant", "content": response.output_text})
```

## Rate limiting (example)

See `rate_limiter.py` for a simple per-process call limiter.

```python
from rate_limiter import RateLimiter

rate_limiter = RateLimiter(max_requests=60, per_seconds=60)
rate_limiter.acquire()
```

## Credits and reference

This project was inspired by the tutorial ["How to Integrate ChatGPT's API With Python Projects"](https://realpython.com/chatgpt-api-python/), by Abdelhadi Dyouri, published by Real Python on January 19, 2026.
