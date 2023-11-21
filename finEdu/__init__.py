from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


import os


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/nuno/FinEdu/instance/finEdu.db'
app.config['SECRET_KEY'] = 'MNGg6tEutTmSq57XgxXOfxeBsaV6zQ1V'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'userLogin'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u"Login é necessário!"

from finEdu.banking import banking_formulas

from finEdu.admin import routes
from finEdu.banking import routes
from finEdu.investments import routes
from finEdu.portfolio import routes
from finEdu.users import routes

from finEdu.users.models import User
from finEdu.portfolio.models import Portfolio, Watchlist




