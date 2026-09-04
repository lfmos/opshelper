# Pitch — OpsHelper AI

O OpsHelper AI é um assistente técnico em Python criado para organizar e recuperar conhecimento de troubleshooting de infraestrutura.

A versão atual recebe uma dúvida, normaliza o texto, identifica termos relevantes e consulta uma base estruturada para retornar:

- categoria;
- possível causa;
- orientação;
- próximo passo.

O projeto cobre cenários de SSH, AWS, Docker, Linux, redes, Git e VPN.

Sua implementação foi mantida propositalmente leve e auditável, sem dependências externas ou uso de LLM em runtime.

O projeto demonstra:

- Python;
- modelagem de conhecimento;
- processamento de texto;
- troubleshooting;
- testes automatizados;
- separação de responsabilidades;
- integração contínua.

O roadmap prevê uma evolução para busca semântica, embeddings e RAG, mantendo respostas fundamentadas na base de conhecimento.