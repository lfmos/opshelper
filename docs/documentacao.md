# Documentação — OpsHelper

## Visão geral

O OpsHelper é um assistente técnico em Python que consulta uma base de conhecimento estruturada para responder dúvidas comuns relacionadas a infraestrutura e operações.

A implementação atual utiliza recuperação determinística de informações e não depende de modelos de linguagem.

## Componentes

### `app.py`

Responsável pela interface de linha de comando.

O módulo:

- recebe a pergunta;
- chama o mecanismo de busca;
- apresenta categoria;
- apresenta possível causa;
- apresenta orientação;
- apresenta próximo passo.

### `src/assistant.py`

Responsável pelo processamento das consultas.

Implementa:

- normalização de caixa;
- remoção de acentos;
- remoção de pontuação;
- tokenização;
- stopwords;
- matching por categoria;
- matching por problema;
- keywords;
- pontuação de relevância;
- fallback para consultas não identificadas.

### `src/knowledge.py`

Responsável pelo carregamento da base JSON.

O caminho é calculado a partir da localização do próprio projeto, evitando dependência do diretório atual do terminal.

### `data/knowledge_base.json`

Armazena os cenários de troubleshooting.

Cada item contém:

- `categoria`;
- `problema`;
- `keywords`;
- `causa`;
- `solucao`;
- `proximo_passo`.

## Fluxo de processamento

```text
Usuário
  |
  v
Pergunta
  |
  v
Normalização
  |
  v
Tokens relevantes
  |
  v
Pontuação dos registros
  |
  v
Melhor correspondência
  |
  v
Resposta estruturada