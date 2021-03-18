from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Jonas'}
    posts = [
        {'author': {'username': 'Jonas'}, 'body': "Oi mozinho"},
        {'author': {'username': 'Eduardo'}, 'body': "Oi meu bb <3"}
    ]
    return render_template("index.html", user=user, posts=posts, title="teste")