from .fixes import fixes


def fixer(fname_trans: str, fname_fixed: str, fixes):
    """Gera arquivo corrigido."""
    # Copia a tradução do Google Translator para o arquivo corrigido
    with open(fname_trans, encoding="utf-8") as f_trans:
        trans = f_trans.read()
    with open(fname_fixed, "w", encoding="utf-8") as f_fixed:
        f_fixed.write(trans)
    # Faz as correções no arquivo corrigido
    for fix in fixes:
        f_trans = open(fname_fixed, encoding="utf-8")
        trans = f_trans.read()
        f_trans.close()
        fixed = trans.replace(fix, fixes[fix])
        f_fixed = open(fname_fixed, "w", encoding="utf-8")
        f_fixed.write(fixed)
        f_fixed.close()
