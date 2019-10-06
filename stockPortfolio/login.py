# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: login.py
# Purpose: Handles the login portion of the stock project.
# Modification: - Add portfolio.html function.
#               - Added Register html function.
#               - Added Forgotten password html function.
#               - Add Profile and transaction function.
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request, flash, session, g

from stockPortfolio import app, db                              # Allow routes to use decorator.

from stockPortfolio.users import User                           # Importing Users Class.
from passlib.hash import pbkdf2_sha256                          # Password Hashing.
from stockPortfolio.forms import RegisterationForm, LoginForm   # Login and Register class functions.
import stockPortfolio.stockAPI as stock                         # Alpha Vantage API.


# Handles the incorrect login info.
@app.errorhandler(405)
def loginError(error):
    return ("Incorrect Username or Password. Please try again!")

@app.route('/login/profile', methods=['GET', 'POST'])
@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    startingUserMoney = 5000
    
    if (request.method == "POST"):
        stockName = request.form['ticker']
        stockQty = request.form['quantity']

        tickerContainer = []
        stock.retrieveDailyStock(stockName)

    return (render_template("profile.html", money=startingUserMoney, title="Profile"))

@app.route('/transaction/')
def transaction():

    return (render_template("transaction.html", title="Transactions"))

@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if (form.validate_on_submit()):
        # Temp login.
        if (form.username.data == "admin" and form.password.data == "admin"):
            flash("Logging you in!", 'success')
            return (redirect(url_for("profile")))
        else:
            return (redirect(url_for("loginError")))

    return (render_template("login.html", title="Login", form=form))

@app.route('/login/register/', methods=['GET', 'POST'])
@app.route('/register/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterationForm()

    if (form.validate_on_submit()):
        # Hashing password immediately to make life easy.
        passwordHashing = pbkdf2_sha256.__hash__(form.password.data)

        # Adding user account onto embedded database.
        user = User(username=form.username.data, password=passwordHashing, email=form.email.data)
        db.session.add(user)
        db.session.commit()

        flash("User Registered onto Database. Please Login!", 'success')
        return (redirect(url_for('login')))

    return (render_template("register.html", title="Register Page", form=form))