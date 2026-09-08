"""Carregamento da base de conhecimento do OpsHelper."""

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KNOWLEDGE_BASE = PROJECT_ROOT / "data" / "knowledge_base.json"


def carregar_base_conhecimento(caminho: Path | str | None = None) -> list[dict]:
    """Carrega e valida a base de conhecimento JSON."""

    caminho_base = Path(caminho) if caminho else DEFAULT_KNOWLEDGE_BASE

    with caminho_base.open("r", encoding="utf-8") as arquivo:
        base = json.load(arquivo)

    if not isinstance(base, list):
        raise ValueError("A base de conhecimento deve conter uma lista de itens.")

    return base