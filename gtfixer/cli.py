"""
Scripts de console
"""
from gtfixer import gtfixer
from gtfixer.fixes import fixes
import click



@click.command()
@click.option("--traducao", "-t", default="traducao.txt", help="Traducao do Google Translator")
@click.option("--correcao", "-c", default="correcao.txt", help="Correcao da traducao")
def cli(traducao, correcao):
    """Corrige traducoes do Google Translator."""
    fix = gtfixer.fixer(traducao, correcao, fixes)
    click.echo("As correcoes foram feitas com sucesso!")
    return 0
