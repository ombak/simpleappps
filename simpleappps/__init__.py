# -*- coding: utf-8 -*-
from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    
    # init database
    db.init_app(app)
    
    # model
    from .models import SimpleAppps

    # register view
    from .views import bp
    app.register_blueprint(bp)

    return app

