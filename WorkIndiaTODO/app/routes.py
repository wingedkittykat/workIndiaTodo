from app import app
from app import db
from werkzeug.urls import url_parse
from flask import render_template, redirect, url_for, flash, request, jsonify, session, abort
from flask_login import current_user, login_user, logout_user
from app.models import user,todo
from app.forms import LoginForm,RegistrationForm

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = user.query.filter_by(id=form.id.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        u = user(id=form.id.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Register Successfully. Sign-in to continue')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form )

@app.route('/addtodo', methods=['get'])
def additem():
    form = TodoForm()
    if form.validate_on_submit():
        u = todo(title=form.title.data,description=form.desc.data,category=form.cat.data,due_date=form.due.data,user_id=form.user.data)
        db.session.add(u)
        db.session.commit()
        flash('added')
        return redirect(url_for('index'))
    return render_template('index.html', title="Todo", form=form )

    
