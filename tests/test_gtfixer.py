from unittest import TestCase
from gtfixer.gtfixer import fixer
from os import path


class TestGTFixer(TestCase):
    def setUp(self):
        self.fixes = {
            "comércio": "trade",
            "faixa de negociação": "lateralidade",
            "vela": "barra",
        }
        fixtures_path = path.join(path.abspath("."), "tests", "fixtures")
        self.f_trans = path.join(fixtures_path, "translation.txt")
        self.f_fixed = path.join(fixtures_path, "fixed.txt")

    def test_gera_uma_traducao_corrigida(self):
        fixer(self.f_trans, self.f_fixed, self.fixes)
        with open(self.f_fixed, encoding="utf-8") as f:
            res = f.read()
        expec = "lateralidade\ntrade\nbarra\n"
        self.assertEqual(res, expec)
