# encoding: utf-8
from fixes import fixes
import sys

filename = sys.argv[1]

for fix in fixes:
    f = open(filename, 'r')
    conteudo = f.read()
    f.close()

    novo = conteudo.replace(fix, fixes[fix])

    f = open(filename, 'w')
    f.write(novo)
    f.close()
