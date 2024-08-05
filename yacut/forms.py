from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Введите вашу ссылку',
        validators=[Length(1, 256), DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Короткая ссылка',
        validators=[Optional(), Length(1, 16), Regexp('[A-Za-z0-9]',
                    message='В ссылке есть недопустимые символы.')])
    submit = SubmitField('Добавить')
