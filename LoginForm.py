from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    ast_name = StringField('id астронавта', validators=[DataRequired()])
    ast_password = PasswordField('пароль астронавта', validators=[DataRequired()])
    cap_name = StringField('id капитана', validators=[DataRequired()])
    cap_password = PasswordField('пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
