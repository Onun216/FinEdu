from finEdu import db, login_manager
from datetime import datetime
from flask_login import UserMixin

import json


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False)
    email = db.Column(db.String(120), unique=False)
    password = db.Column(db.String(180), unique=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name


