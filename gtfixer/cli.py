import click
from gtfixer.gtfixer import fixer
from gtfixer.fixes import fixes


@click.command()
@click.option(
    "--translation", "-t", default="trans.txt", help="Arquivo que contem a tradução"
)
@click.option(
    "--fixed", "-f", default="fixed.txt", help="Arquivo que conterá a correção"
)
def fix(translation, fixed):
    click.echo(fixer(translation, fixed, fixes))
    return 0
