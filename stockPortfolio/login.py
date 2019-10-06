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

from stockPortfolio import app, db, bcrypt                      # Allow routes to use decorator.

from stockPortfolio.models import User                          # Importing Users Class.
from stockPortfolio.forms import RegisterationForm, LoginForm   # Login and Register class functions.
from stockPortfolio.stockForms import EnteringStock             # Stock class functions.
from flask_login import login_user, current_user, logout_user   # Login manager.
import stockPortfolio.stockAPI as stock                         # Alpha Vantage API.


# Handles the incorrect login info.
@app.errorhandler(405)
def loginError(error):
    return ("Incorrect Username or Password. Please try again!")

@app.route('/login/profile', methods=['GET', 'POST'])
@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    # If user is not logged in, we don't want them to see profile or transactions at all.
    if current_user.is_authenticated == False:
        return redirect(url_for('login'))

    startingUserMoney = 5000
    
    if (request.method == "POST"):
        stockName = request.form['ticker']
        stockQty = request.form['quantity']

        tickerContainer = []
        stock.retrieveDailyStock(stockName)

    return (render_template("profile.html", money=startingUserMoney, title="Profile"))

    # Creating instance of form.
    # form = EnteringStock()

    # if (form.validate_on_submit()):
    #     pass

@app.route('/transaction/')
def transaction():
    # If user is not logged in, we don't want them to see profile or transactions at all.
    if current_user.is_authenticated == False:
        return redirect(url_for('login'))

    return (render_template("transaction.html", title="Transactions"))

@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()

    if (form.validate_on_submit()):
        user = User.query.filter_by(username=form.username.data).first()

        if (user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user)
            redirect(url_for('profile'))
        else:
            flash ("Login Unsuccessful.", "danger")
    
    return (render_template("login.html", title="Login", form=form))

@app.route('/login/register/', methods=['GET', 'POST'])
@app.route('/register/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = RegisterationForm()

    if (form.validate_on_submit()):
        # Hashing password immediately to make life easy.
        passwordHashing = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Adding user account onto embedded database.
        user = User(username=form.username.data, password=passwordHashing, email=form.email.data)
        db.session.add(user)
        db.session.commit()

        flash("User Registered onto Database. Please Login!", 'success')
        return (redirect(url_for("login")))

    return (render_template("register.html", title="Register", form=form))

@app.route("/logout/")
def logout():
    logout_user()

    return redirect(url_for("login"))