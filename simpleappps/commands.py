# -*- coding:utf-8 -*-
import click
from flask.cli import with_appcontext
from simpleappps import db


@click.command('init-db')
@with_appcontext
def init_db():
    db.create_all()


def init_app(app):
    app.cli.add_command(init_db)
