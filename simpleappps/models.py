# -*- coding:utf-8 -*-
from simpleappps import db


class SimpleAppps(db.Model):
    __tablename__ = 'simpleapps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(1028))

