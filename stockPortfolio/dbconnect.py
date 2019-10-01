# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: dbconnect.py
# Purpose: Sqlite3 allows us to have an embedded database where we can store login credentials.
# Modification: 
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request
from stockPortfolio import app
from flask import g

import sqlite3

# Database path
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Closing connection to database.
@app.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, "_database", None)

    if db is not None:
        db.close()

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS users(unid INT(11) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(25), password VARCHAR(25), email VARCHAR(50))")

def insertTable(data):
    insertStatement = "INSERT INTO TABLE {} VALUES()".format('users')

    c.execute(insertStatement)
    conn.commit()

    c.close()
    conn.close()