from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data

        if not short:
            short = get_unique_short_id()

        elif URLMap.query.filter_by(short=short).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)

        urlmap = URLMap(
            original=form.original_link.data,
            short=short
        )

        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', form=form, short=short)

    return render_template('index.html', form=form)


@app.route('/<string:custom_id>')
def redirect_custom_id(custom_id):
    urlmap = URLMap.query.filter_by(short=custom_id).first_or_404()
    return redirect(urlmap.original)