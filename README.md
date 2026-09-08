# OpsHelper

Assistente técnico em Python baseado em conhecimento estruturado para troubleshooting de infraestrutura, Linux, Docker, AWS, Git, redes e VPN.

O OpsHelper foi desenvolvido como um projeto prático para organizar conhecimento técnico e transformar dúvidas comuns de infraestrutura em respostas estruturadas com possível causa, orientação e próximo passo.

> A versão atual utiliza busca determinística por tokens e palavras-chave. Integrações com IA generativa, embeddings e RAG fazem parte do roadmap e não são apresentadas como funcionalidades já implementadas.

---

## Objetivo

O projeto busca demonstrar:

- Python aplicado a troubleshooting;
- organização de uma base de conhecimento;
- normalização de texto;
- matching determinístico;
- respostas estruturadas;
- separação entre interface, lógica e dados;
- testes automatizados;
- integração contínua;
- documentação de limitações técnicas.

---

## Como funciona

    Pergunta do usuário
            |
            v
    Normalização de texto
            |
            v
    Extração de tokens
            |
            v
    Base de conhecimento JSON
            |
            v
    Pontuação de relevância
            |
            v
    Melhor correspondência
            |
            v
    Resposta estruturada

A resposta apresenta:

- categoria;
- possível causa;
- orientação;
- próximo passo.

Quando não existe correspondência suficientemente confiável, o assistente informa que não possui dados suficientes em sua base.

---

## Tecnologias

- Python 3.11+
- JSON
- unittest
- Git
- GitHub
- GitHub Actions

A aplicação não exige bibliotecas externas para execução.

---

## Categorias atuais

A base contém cenários relacionados a:

- SSH;
- AWS / EC2;
- Docker;
- Linux;
- Redes;
- Git;
- VPN.

Cada registro pode utilizar palavras-chave adicionais para melhorar a recuperação da informação.

---

## Exemplo

Pergunta:

    Meu Docker? O container não funciona.

Resposta esperada:

    Categoria: Docker

    Possível causa:
    O container pode estar parado, apresentar erro na aplicação
    ou possuir configuração incorreta.

    Orientação:
    Utilize docker ps -a para verificar o status e docker logs
    nome_do_container para analisar mensagens de erro.

    Próximo passo:
    Identificar o erro apresentado nos logs antes de reiniciar o serviço.

---

## Estrutura

    opshelper/
    ├── app.py
    ├── data/
    │   └── knowledge_base.json
    ├── src/
    │   ├── assistant.py
    │   └── knowledge.py
    ├── tests/
    │   └── test_assistant.py
    ├── docs/
    │   ├── documentacao.md
    │   ├── metricas.md
    │   ├── pitch.md
    │   └── prompt.md
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── .gitignore
    ├── requirements.txt
    ├── LICENSE
    └── README.md

---

## Executando localmente

Clone o repositório:

    git clone https://github.com/lfmos/opshelper.git
    cd opshelper

Execute:

    python app.py

Não é necessário instalar dependências externas para utilizar a versão atual.

---

## Testes

O projeto possui testes automatizados com `unittest`.

Execute:

    python -m unittest discover -s tests -v

Os testes validam:

- remoção de acentos;
- normalização de caixa;
- consultas SSH;
- AWS / EC2;
- Docker;
- Linux;
- Redes;
- Git;
- consulta fora do escopo;
- presença de causa na resposta;
- carregamento da base independente do diretório atual.

---

## Qualidade de código

Para verificar se os módulos compilam corretamente:

    python -m compileall app.py src tests

O workflow do GitHub Actions executa automaticamente os testes e a validação de compilação.

---

## Limitações atuais

A versão atual:

- não utiliza LLM em runtime;
- não utiliza embeddings;
- não realiza busca vetorial;
- não consulta serviços externos;
- depende do conteúdo previamente definido na base de conhecimento;
- utiliza scoring determinístico para escolher a resposta.

Essas limitações são intencionais e mantêm a implementação simples, auditável e sem dependências externas.

---

## Roadmap

Possíveis evoluções:

- expansão da base de conhecimento;
- busca semântica;
- embeddings;
- integração com LLM;
- RAG;
- histórico de conversas;
- interface web;
- classificação de confiança;
- fontes e referências por resposta.

Uma futura versão com IA generativa deverá manter respostas fundamentadas na base de conhecimento e evitar geração de comandos não suportados pelos dados disponíveis.

---

## Segurança

O OpsHelper fornece orientações técnicas educacionais.

Comandos devem ser revisados antes de utilização em ambientes reais, principalmente quando envolverem:

- permissões;
- redes;
- cloud;
- containers;
- acesso remoto;
- serviços críticos.

---

## Autor

Projeto desenvolvido como parte de um portfólio prático de tecnologia, infraestrutura, automação e cibersegurança.