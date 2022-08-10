from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luciano'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Mais um dia de chuva em Joinville'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Qual será o próximo filme da Marvel?'
        },
        {
            'author': {'username': 'Jack'},
            'body': 'Jogar em consoles ou pc?'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template("login.html", form=form)
