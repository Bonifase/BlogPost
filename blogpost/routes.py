from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user
from blogpost import app, db, bcrypt
from blogpost.forms.forms import RegistrationForm, LoginForm
from blogpost.models.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf')
        user = User(
            username=form.username.data, email=form.email.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'{form.username.data} accout has been created! You can login',
            'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # noqa
            login_user(user, remember=form.remember.data)
            flash(
                f'You logged in successfully for {user.username}!',
                'success')
            return redirect(url_for('home'))
        flash(
            f'Invalid login credentials',
            'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
