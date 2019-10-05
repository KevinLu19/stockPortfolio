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
from flask_login import login_user, logout_user, current_user, login_required, LoginManager

from stockPortfolio import app                  # Allow routes to use decorator.

from passlib.hash import sha256_crypt           # Password Hashing. 
import stockPortfolio.dbconnect as dataBase     # Database.
import stockPortfolio.users                     # Importing Users Class.
import stockPortfolio.stockAPI as stock         # Alpha Vantage API.


# Initialize loginManger to app instance. Need this to make them work together.
loggingManage = LoginManager()
loggingManage.init_app(app)
loggingManage.login_view = 'login'

# Handles the incorrect login info.
@app.errorhandler(405)
def loginError(error):
    return ("Incorrect Username or Password. Please try again!")

@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    startingUserMoney = 5000
    
    if (request.method == "POST"):
        stockName = request.form['ticker']
        stockQty = request.form['quantity']

        tickerContainer = []
        stock.retrieveDailyStock(stockName)
        # tickerContainer.append(tickerName)
        

    return (render_template("profile.html", money=startingUserMoney))

@app.route('/transaction/')
def transaction():

    return (render_template("transaction.html"))

@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = ""

    try:
        if (request.method == "POST"):
            attemptUsername = request.form['username']
            attemptPassword = request.form['password']

            dataBase.insertUser(attemptUsername, attemptPassword)
            users = dataBase.retrieveUsers()

            if (users == dataBase.retrieveUsers()):
                return (redirect(url_for('profile')))
            else:
                error = "Invalid Credentials. Please Try Again!"
                return (redirect(url_for('loginError')))

        return (render_template("login.html", error=error))
    
    except Exception as e:
        return (render_template("login.html", error=error))


@app.route('/login/register/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
@app.route('/register/', methods=['GET', 'POST'])
def register():

    if (request.method == "POST"):
            user = request.form['username']
            password = request.form['passowrd']
            email = request.form['email']

            dataBase.insertRegistredUser(user, password, email)
            flash("User Registered onto Database.")

            return (redirect(url_for('login')))

    else:
        return (render_template("register.html", title="register"))