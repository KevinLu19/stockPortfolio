# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: login.py
# Purpose: Handles the login portion of the stock project.
# Modification: - Add portfolio.html function.
#               - Added Register html function.
#               - Added Forgotten password html function.
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request
from stockPortfolio import app
from flask import g

import stockPortfolio.dbconnect

# Handles the incorrect login info.
@app.errorhandler(405)
def loginError(error):
    return ("Incorrect Username or Password. Please try again!")

@app.route('/profile/')
def profile():
    startingUserMoney = 5000
    return (render_template("profile.html", userMoney=startingUserMoney))


@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = ""

    try:
        if (request.method == "POST"):
            attemptUsername = request.form['username']
            attemptPassword = request.form['password']
            
            # Temporary stuff. Just testing login.
            if (attemptUsername == "admin" and attemptPassword == "password"):
                return (redirect(url_for('profile')))
            else:
                error = "Invalid Credntials. Please try again!"
                return (redirect(url_for("loginError")))
        return (render_template("login.html", error=error))
    
    except Exception as e:
        return (render_template("login.html", error=error))


@app.route('/login/register/')
@app.route('/register/', methods=['GET', 'POST'])
def register():
    return (render_template("register.html", title="register"))