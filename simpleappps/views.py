# -*- coding: utf-8 -*-
from flask import Blueprint, request, url_for, render_template
from simpleappps import db
from .models import SimpleAppps
from .forms import SimpleAppForms


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleAppForms()
    if request.method == 'POST':
        simpleapp = SimpleAppps(
            name=form.name.data,
            url=form.url.data
        )
        db.session.add(simpleapp)
        db.session.commit()
    
    return render_template(
        'index.html',
        form=form,
        title='Simple Apps',
        simple_list=SimpleAppps.query.all()
    )
