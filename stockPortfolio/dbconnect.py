# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: dbconnect.py
# Purpose: Sqlite3 allows us to have an embedded database where we can store login credentials.
# Modification: - Added Users class to store user login info.
#               - Moved Creating table on it's own separate file.
# ----------------------------------------------------------------------------------------

import sqlite3 as sql

# Used for inserting information when user tries to register for an account.
def insertRegistredUser(username, password, email):
    con = sql.connect("users.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
    con.commit()
    con.close()

# Used for inserting login info.
def insertUser(username, password):
    con = sql.connect("users.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()

    con.close()

    return (users)

# # Used for checking if users with same email has already registered.
# def queryRegisterUser():
#     conn = sql.connect("users.db")
#     c = conn.cursor()
    
#     c.execute("SELECT username, password, email FROM users")
#     registeredUser = c.fetchall()

#     conn.close()

#     return (registeredUser)