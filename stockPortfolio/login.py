

from flask import render_template
from stockPortfolio import app

@app.route('/')
@app.route('/login')
def login():
    return (render_template("login.html"))