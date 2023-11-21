from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, ValidationError, \
    IntegerField
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from finEdu.users.models import Portfolio, Watchlist




class PortfolioRegistrationForm(FlaskForm):
    portfolio_name = StringField('Nome', [validators.Length(min=4, max=25)])      
    submit = SubmitField('Guardar')


class WatchlistRegistrationForm(FlaskForm):
    watchlist_name = StringField('Nome', [validators.Length(min=4, max=25)])  
    submit = SubmitField('Guardar')
