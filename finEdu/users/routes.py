from flask import request, flash, render_template, session, url_for, redirect, make_response
from flask_login import login_user, logout_user, current_user, login_required

from finEdu import app, db, bcrypt, login_manager
from finEdu.users.forms import UserRegistrationForm, UserLoginForm
from finEdu.users.models import User
from finEdu.portfolio.models import Portfolio, Watchlist

import json
import os


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(name=form.name.data,
                        email=form.email.data,
                        password=hash_password)
        db.session.add(new_user)
        flash('Novo cliente criado com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('userLogin'))
    return render_template('users/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def userLogin():
    form = UserLoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and bcrypt.check_password_hash(attempted_user.password, form.password.data):
            login_user(attempted_user)
            # session['email'] = form.email.data
            # flash(f'Login bem sucedido!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('portfolio_home', id=current_user.id))
        else:
            flash('Dados incorrectos! Tente novamente', 'danger')

    return render_template('users/login.html', form=form)


@app.route('/user-account/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user_account(id):
    form = UserRegistrationForm()
    user = User.query.filter_by(id=current_user.id).first()

    if request.method == 'POST':
        user.name = form.name.data
        user.email = form.email.data

        flash(f'Dados actualizados com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('user_account', id=current_user.id))

    form.name.data = user.name
    form.email.data = user.email
    # form.password.data = user.password

    return render_template('users/user_account.html', form=form, user=user)


@app.route('/logout')
def user_logout():
    logout_user()
    session.pop('new_constituents', None)
    return redirect(url_for('home'))
