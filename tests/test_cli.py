from unittest import TestCase
from click.testing import CliRunner
from gtfixer.cli import fix
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
        self.f_trans = path.join(fixtures_path, "translation.txt")
        self.f_fixed = path.join(fixtures_path, "fixed.txt")

    def test_gera_um_arquivo_corrigido(self):
        res = self.runner.invoke(fix, ["-t", self.f_trans, "-f", self.f_fixed])
        expec = "\n"
        self.assertEqual(res.output, expec)
        self.assertEqual(res.exit_code, 0)
