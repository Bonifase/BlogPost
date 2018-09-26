from flask import render_template, flash, redirect, url_for
from blogpost import app
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Account created for {form.username.data} !',
            'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data and form.password.data:
            flash(
                f'You logged in successfully for {form.email.data} !',
                'success')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)