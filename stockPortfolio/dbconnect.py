# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: dbconnect.py
# Purpose: Sqlite3 allows us to have an embedded database where we can store login credentials.
# Modification: - Added Users class to store user login info.
#               - Moved Creating table on it's own separate file.
# ----------------------------------------------------------------------------------------

from stockPortfolio import app
from flask_sqlalchemy import SQLAlchemy

import sqlite3 as sql

# Database path & connect to database.
db = SQLAlchemy(app)

# Used for inserting information when user tries to register for an account.
def insertRegistredUser(username, password, email):
    conn = sql.connect("users.db")
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))

    conn.commit()
    conn.close()

# Used for inserting login info.
def insertUser(username, password):
    conn = sql.connect("users.db")
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def retrieveUsers():
    conn = sql.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT username, password FROM users")
    users = c.fetchall()
    conn.close()

    return (users)

# # Used for checking if users with same email has already registered.
# def queryRegisterUser():
#     conn = sql.connect("users.db")
#     c = conn.cursor()
    
#     c.execute("SELECT username, password, email FROM users")
#     registeredUser = c.fetchall()

#     conn.close()

#     return (registeredUser)