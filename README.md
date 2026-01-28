# chatgpt-api-python

Pequenos exemplos de uso do OpenAI SDK em Python.

## Configuracao rapida
1. Crie um arquivo `.env` baseado em `.env.example` e defina `OPENAI_API_KEY`.
2. Instale as dependências com o seu gerenciador preferido.
3. Rode um dos scripts de exemplo.

## Exemplos
- `basic_chatgpt_call.py`: chamada simples.
- `coding_assistant.py`: assistente interativo.
- `structured_output.py`: saída estruturada com Pydantic.

## Consideracoes de seguranca
- Mantenha suas chaves de API seguras. Use variáveis de ambiente ou servicos de gerenciamento de chaves em produção.
- Nunca envie chaves de API para o controle de versão e rotacione-as regularmente se houver suspeita de vazamento.
- Considere implementar limitação de taxa nas suas aplicações para evitar custos inesperados.

## Gestao de custos
- Monitore o uso e os custos no dashboard da OpenAI.
- Modelos diferentes têm preços diferentes e o custo acumula pelo número de tokens processados (entrada e saída).
- Avalie o trade-off entre capacidade do modelo e custo para cada caso de uso.
- Em desenvolvimento, você pode usar endpoints mock gratuitos (como o OpenAI mock API do Beeceptor) para testar a integração sem custos.
- Ao usar mocks de terceiros, utilize uma chave fictícia e evite enviar dados sensíveis.

### Mock de API (opcional)
Para apontar seus testes para um mock, configure `OPENAI_BASE_URL` no `.env`. O SDK usa essa variável automaticamente.

## Limitacao de taxa (exemplo)
Veja `rate_limiter.py` para um limitador simples de chamadas por processo.

```python
from rate_limiter import RateLimiter

rate_limiter = RateLimiter(max_requests=60, per_seconds=60)
rate_limiter.acquire()
```
