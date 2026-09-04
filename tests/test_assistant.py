import os
import tempfile
import unittest

from src.assistant import (
    buscar_resposta,
    normalizar_texto,
)
from src.knowledge import carregar_base_conhecimento


class TestNormalizacao(unittest.TestCase):

    def test_remove_acentos_e_pontuacao(self):
        self.assertEqual(
            normalizar_texto("Permissão SSH?"),
            "permissao ssh",
        )

    def test_normaliza_caixa(self):
        self.assertEqual(
            normalizar_texto("DOCKER"),
            "docker",
        )


class TestBuscaResposta(unittest.TestCase):

    def test_identifica_ssh(self):
        resposta = buscar_resposta(
            "Estou recebendo permission denied no SSH"
        )
        self.assertEqual(resposta["categoria"], "SSH")

    def test_identifica_aws_ec2(self):
        resposta = buscar_resposta(
            "Não consigo acessar minha instância EC2"
        )
        self.assertEqual(resposta["categoria"], "AWS")

    def test_identifica_docker_com_pontuacao(self):
        resposta = buscar_resposta(
            "Meu Docker? O container não funciona."
        )
        self.assertEqual(resposta["categoria"], "Docker")

    def test_identifica_linux(self):
        resposta = buscar_resposta(
            "Meu usuário está sem permissão para executar uma ação"
        )
        self.assertEqual(resposta["categoria"], "Linux")

    def test_identifica_rede(self):
        resposta = buscar_resposta(
            "O serviço não está acessível pela porta 8080"
        )
        self.assertEqual(resposta["categoria"], "Rede")

    def test_identifica_git(self):
        resposta = buscar_resposta(
            "Fiz commit mas as alterações não aparecem no GitHub"
        )
        self.assertEqual(resposta["categoria"], "Git")

    def test_consulta_fora_do_escopo(self):
        resposta = buscar_resposta(
            "Minha impressora está sem tinta"
        )
        self.assertEqual(
            resposta["categoria"],
            "Não identificado",
        )

    def test_resposta_inclui_causa(self):
        resposta = buscar_resposta(
            "Problema com container Docker"
        )
        self.assertIn("causa", resposta)
        self.assertTrue(resposta["causa"])


class TestKnowledgeBase(unittest.TestCase):

    def test_carregamento_independe_do_diretorio_atual(self):
        diretorio_original = os.getcwd()

        with tempfile.TemporaryDirectory() as diretorio:
            try:
                os.chdir(diretorio)
                base = carregar_base_conhecimento()

                self.assertGreater(len(base), 0)

            finally:
                os.chdir(diretorio_original)


if __name__ == "__main__":
    unittest.main()