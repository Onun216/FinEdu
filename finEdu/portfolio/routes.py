import numpy as np
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib
import json
import plotly
import plotly.graph_objects as go
import secrets

from itertools import groupby
from datetime import timedelta


from finEdu import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required


from finEdu.finData.portfolio_info import constituents
from finEdu.users.models import User
from finEdu.portfolio.models import Portfolio, Watchlist

from finEdu.portfolio.portfolio_dividends import get_dividends, dividends_growth, dividends_per_year


@app.route('/portfolio-home', methods=['GET', 'POST'])
@login_required
def portfolio_home():

    return render_template('portfolio/portfolio_home.html')


@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def user_portfolio():
    current_portfolio = Portfolio.query.filter_by(
        user_id=current_user.id).first()
    if current_user.is_authenticated and request.method == 'GET':
        # Apply Class method to group constituents by ticker
        portfolio = current_portfolio.group_portfolio_constituents()
        # Get dividends per year
        dividends = dividends_per_year(get_dividends(), 2022)
        div_growth = dividends_growth(dividends)

    try:
        if current_user.is_authenticated and request.method == 'POST':
            if not current_portfolio and 'new_constituents' in session:
                # Portfolio is created with name as MyPortfolio
                portfolio = Portfolio(portfolio_name='MyPortfolio',
                                      constituents=session['new_constituents'],
                                      user_id=current_user.id)
                db.session.add(portfolio)
                db.session.commit()
                session.pop('new_constituents')
                return redirect(request.referrer)

            else:
                # Updates current_portfolio sotred in database
                current_portfolio.update_portfolio_constituents(
                    session['new_constituents'])
                session.pop('new_constituents')
                return redirect(request.referrer)

    except Exception as e:
        print(e)

    return render_template('portfolio/user_portfolio.html', portfolio=portfolio,
                           div_growth=div_growth)


@app.route('/add-constituent', methods=['POST'])
@login_required
def add_constituent():
    # Session variable acts like a Global variable
    try:
        user_id = current_user.id
        ticker = request.form.get("constituent-ticker")
        quantity = request.form.get("constituent-quantity")
        price = request.form.get("constituent-price")
        date = request.form.get("purchase-date")

        if ticker and quantity and price and date and request.method == 'POST':
            operation_code = secrets.token_hex(5)
            new_constituent = {operation_code: {ticker: {'price': float(price),
                                                         'quantity': int(quantity),
                                                         'date': date}}}
            if 'new_constituents' in session:
                # Merge session (dict) with new_constituent (dict)
                session['new_constituents'] = session['new_constituents'] | new_constituent
                print(session['new_constituents'])
                return redirect(request.referrer)

            else:
                # Create session (dict) with new_contituent
                session['new_constituents'] = new_constituent
                print(session['new_constituents'])
                return redirect(request.referrer)

    except Exception as e:
        print(e)

    finally:
        return redirect(request.referrer)


@app.route('/remove-constituent/<operation_code>')
def remove_constituent(operation_code):
    if 'new_constituents' in session:
        try:
            session.modified = True
            for key, value in session['new_constituents'].items():
                if key == operation_code:
                    # print(key)
                    session['new_constituents'].pop(key, None)
                    return redirect(url_for('user_portfolio'))

        except Exception as e:
            print(e)
            return redirect(url_for('user_portfolio'))


@app.route('/remove-from-portfolio/<operation_code>', methods=['POST'])
@login_required
def remove_from_portfolio(operation_code):
    user_id = current_user.id
    current_portfolio = Portfolio.query.filter_by(
        user_id=current_user.id).first()
    
    

    if current_user.is_authenticated:
        try:
            current_portfolio.delete_portfolio_constituents(current_portfolio,
                                                            operation_code)
            return redirect(url_for('user_portfolio'))

        except Exception as e:
            print(e)
            return redirect(url_for('user_portfolio'))
