# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField


class SimpleAppForms(FlaskForm):
    id = HiddenField(u'Id')
    name = StringField(u'Name')
    url = StringField(u'URL')
