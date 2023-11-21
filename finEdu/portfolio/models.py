from finEdu import db, login_manager
from datetime import datetime

import json


class JsonEncodeDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_name = db.Column(db.String(30), unique=False)
    constituents = db.Column(JsonEncodeDict)
    # constituents_sales = db.Column(JsonEncodeDict)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship('User',
                           backref=db.backref('portfolios', lazy=True))

    def __repr__(self):
        return '<Portfolio %r>' % self.portfolio_name

    def update_portfolio_constituents(self, dict):
        self.constituents = self.constituents | dict
        db.session.commit()

    def group_portfolio_constituents(self):
        grouped_portfolio = {}
        for operation_code, operation_data in self.constituents.items():
            for ticker, trade_data in operation_data.items():
                if ticker not in grouped_portfolio:
                    grouped_portfolio[ticker] = []
                grouped_portfolio[ticker].append({
                    'date': trade_data['date'],
                    'price': trade_data['price'],
                    'quantity': trade_data['quantity'],
                    'operation_code': operation_code,
                })
        return grouped_portfolio
    
    def delete_portfolio_constituents(self, code) -> None:
        for operation_code, operation_data in self.constituents.items():  
            if operation_code == code:        
                self.constituents.pop(operation_code, None)
                db.session.commit()
            

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    watchlist_name = db.Column(db.String(30), unique=False)
    constituents = db.Column(JsonEncodeDict)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship('User',
                           backref=db.backref('watchlists', lazy=True))

    def __repr__(self):
        return '<Watchlist %r>' % self.watchlist_name
