"""Lógica de busca determinística do OpsHelper."""

import re
import unicodedata

from src.knowledge import carregar_base_conhecimento


STOPWORDS = {
    "a",
    "as",
    "ao",
    "aos",
    "como",
    "com",
    "da",
    "das",
    "de",
    "do",
    "dos",
    "e",
    "em",
    "esta",
    "estou",
    "meu",
    "minha",
    "na",
    "nas",
    "no",
    "nos",
    "o",
    "os",
    "para",
    "por",
    "que",
    "um",
    "uma",
}


def normalizar_texto(texto: str) -> str:
    """Normaliza caixa, acentos, pontuação e espaços."""

    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]+", " ", texto)

    return " ".join(texto.split())


def encontrar_palavras_chave(texto: str) -> set[str]:
    """Extrai tokens relevantes de uma pergunta."""

    return {
        palavra
        for palavra in normalizar_texto(texto).split()
        if len(palavra) > 1 and palavra not in STOPWORDS
    }


def pontuar_item(
    pergunta_normalizada: str,
    palavras_usuario: set[str],
    item: dict,
) -> int:
    """Calcula a relevância de um item da base para a pergunta."""

    pontuacao = 0

    categoria = normalizar_texto(item.get("categoria", ""))

    if categoria in palavras_usuario:
        pontuacao += 4

    palavras_problema = encontrar_palavras_chave(
        item.get("problema", "")
    )

    pontuacao += len(palavras_usuario & palavras_problema)

    for keyword in item.get("keywords", []):
        keyword_normalizada = normalizar_texto(keyword)

        if not keyword_normalizada:
            continue

        if " " in keyword_normalizada:
            if keyword_normalizada in pergunta_normalizada:
                pontuacao += 3
        elif keyword_normalizada in palavras_usuario:
            pontuacao += 2

    return pontuacao


def resposta_nao_identificada() -> dict:
    """Retorna a resposta padrão para consultas fora da base."""

    return {
        "categoria": "Não identificado",
        "causa": "Não há informação suficiente na base de conhecimento.",
        "resposta": (
            "Não encontrei uma orientação confiável para essa consulta."
        ),
        "proximo_passo": (
            "Forneça mais detalhes ou consulte a documentação oficial "
            "da tecnologia envolvida."
        ),
    }


def buscar_resposta(pergunta: str) -> dict:
    """Busca o item mais relevante na base de conhecimento."""

    if not isinstance(pergunta, str) or not pergunta.strip():
        return resposta_nao_identificada()

    base = carregar_base_conhecimento()

    pergunta_normalizada = normalizar_texto(pergunta)
    palavras_usuario = encontrar_palavras_chave(pergunta)

    melhor_resultado = None
    maior_pontuacao = 0

    for item in base:
        pontuacao = pontuar_item(
            pergunta_normalizada,
            palavras_usuario,
            item,
        )

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resultado = item

    # Exige mais do que uma coincidência trivial.
    if melhor_resultado is None or maior_pontuacao < 2:
        return resposta_nao_identificada()

    return {
        "categoria": melhor_resultado["categoria"],
        "causa": melhor_resultado["causa"],
        "resposta": melhor_resultado["solucao"],
        "proximo_passo": melhor_resultado["proximo_passo"],
    }