from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post


posts = [
    {
        'author': 'Rayan Hussain',
        'title': 'Image Post 1',
        'content': 'Picture of socks',
        'date_posted': 'December 22, 2020'
    },
    {
        'author': 'Monster Hunter',
        'title': 'Image Post 2',
        'content': 'Picture of monster',
        'date_posted': 'December 23, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successful!', 'success')
        return redirect(url_for('home'))
    elif not form.validate_on_submit:
        flash('Login Failed! Please check Email and Password!', 'danger')

    return render_template('login.html', title='Login', form=form)

