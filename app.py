"""Interface de linha de comando do OpsHelper."""

from src.assistant import buscar_resposta


def exibir_resposta(resposta: dict) -> None:
    """Exibe uma resposta estruturada no terminal."""

    print("\nOpsHelper:")
    print(f"Categoria: {resposta['categoria']}")
    print(f"\nPossível causa: {resposta['causa']}")
    print(f"\nOrientação: {resposta['resposta']}")
    print(f"\nPróximo passo: {resposta['proximo_passo']}")
    print("-" * 50)


def iniciar_assistente() -> None:
    """Inicia a interface interativa do assistente."""

    print("=" * 50)
    print("OpsHelper - Assistente Técnico")
    print("=" * 50)

    print("\nDigite sua dúvida técnica.")
    print("\nExemplos de perguntas:")
    print("- Erro de permissão SSH")
    print("- Problemas com Docker")
    print("- Acesso à instância EC2")
    print("- Dúvidas sobre Git")
    print("- Problemas de rede")
    print("\nDigite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Usuário: ").strip()

        if pergunta.casefold() == "sair":
            print("\nEncerrando OpsHelper. Até mais!")
            break

        if not pergunta:
            print("\nDigite uma pergunta antes de continuar.")
            continue

        resposta = buscar_resposta(pergunta)
        exibir_resposta(resposta)


if __name__ == "__main__":
    iniciar_assistente()