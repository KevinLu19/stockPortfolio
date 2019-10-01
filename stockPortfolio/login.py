# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: login.py
# Purpose: Handles the login portion of the stock project.
# Modification: - Add portfolio.html function.
#               - Added Register html function.
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request
from stockPortfolio import app
from flask import g


# Handles the incorrect login info.
@app.errorhandler(405)
def loginError(error):
    return ("Incorrect Username or Password. Please try again!")

@app.route('/profile/')
def profile():
    return (render_template("profile.html"))


@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = ""

    try:
        if (request.method == "POST"):
            attemptUsername = request.form['username']
            attemptPassword = request.form['password']

            if (attemptUsername == "admin" and attemptPassword == "password"):
                return (redirect(url_for('profile')))
            else:
                error = "Invalid Credntials. Please try again!"
                return (redirect(url_for("loginError")))
        return (render_template("login.html", error=error))
    
    except Exception as e:
        return (render_template("login.html", error=error))


@app.route('/login/register/', methods=['GET', 'POST'])
def register():
    pass