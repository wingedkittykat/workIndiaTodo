from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,ValidationError,EqualTo
from app.models import user

class LoginForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    def validate_id(self, id):
        u = user.query.filter_by(id=id.data).first()
        if u is not None:
            raise ValidationError('Agent already exists')

class RegistrationForm(FlaskForm):
    id = StringField('Agent Id', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    