# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: dbconnect.py
# Purpose: Connect to mysql database.
# Modification: 
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request
from stockPortfolio import app
from flask import g

import sqlite3

# Database path
conn = "/path/to/database.db"

# Connecting to database.
def connection():
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = sqlite3.connect(conn)
    
    return (db)

# Closing connection to database.
@app.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, "_database", None)

    if db is not None:
        db.close()

def createTable():
    c = connection().cursor()

    table = c.execute('''CREATE TABLE users (unid INT(11) AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(25), password VARCHAR(25), email VARCHAR(50)) ''')

    return (table)

