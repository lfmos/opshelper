# Validação e Métricas — OpsHelper

## Estratégia de validação

A versão atual possui testes automatizados utilizando `unittest`.

Os testes verificam o comportamento do mecanismo de normalização, recuperação de conhecimento e tratamento de consultas fora do escopo.

## Casos automatizados

| Caso | Resultado esperado |
| --- | --- |
| `Permissão SSH?` | normalização para `permissao ssh` |
| `DOCKER` | normalização para `docker` |
| erro `permission denied` no SSH | categoria SSH |
| problema de acesso EC2 | categoria AWS |
| container Docker com pontuação | categoria Docker |
| usuário sem permissão | categoria Linux |
| serviço inacessível por porta | categoria Rede |
| commit não aparece no GitHub | categoria Git |
| impressora sem tinta | Não identificado |
| resposta Docker | inclui possível causa |
| execução fora da raiz do projeto | base continua carregando |

## Execução

    python -m unittest discover -s tests -v

A validação também inclui:

    python -m compileall app.py src tests

e:

    git diff --check

## Interpretação

O objetivo dos testes não é medir inteligência artificial, pois a versão atual não utiliza um modelo de IA.

Eles validam:

- consistência;
- normalização;
- recuperação determinística;
- robustez básica;
- fallback;
- independência do diretório de execução.

## Limitações das métricas

A base atual é pequena e controlada.

Por isso, estes testes não representam:

- benchmark de NLP;
- precisão estatística em dataset amplo;
- desempenho de LLM;
- avaliação de RAG;
- cobertura de troubleshooting de produção.

Esses tipos de avaliação exigiriam uma versão futura com escopo e dataset maiores.