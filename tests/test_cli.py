from unittest import TestCase
from click.testing import CliRunner
from gtfixer import cli
from os import path


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.fixes = {
            "comércio": "trade",
            "faixa de negociação": "lateralidade",
            "vela": "barra",
        }
        fixtures_path = path.join(path.abspath("."), "tests", "fixtures")
        self.f_trans = path.join(fixtures_path, "traducao.txt")
        self.f_fixed = path.join(fixtures_path, "correcao.txt")

    def test_gera_um_arquivo_corrigido(self):
        res = self.runner.invoke(cli.cli, ["-t", self.f_trans, "-c", self.f_fixed])
        expec = "As correcoes foram feitas com sucesso!\n"
        self.assertEqual(res.output, expec)
        self.assertEqual(res.exit_code, 0)
