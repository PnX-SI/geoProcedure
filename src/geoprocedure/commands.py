import click
from flask.cli import with_appcontext


@click.group(help="Manager demarche simplifier api.")
def get_data():
    pass


@get_data.command()
@with_appcontext
def info():
    print("yoyoyo j'aime les données")
