from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Luciano'}
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
    return render_template("index.html",title='Home', user=user, posts=posts)

