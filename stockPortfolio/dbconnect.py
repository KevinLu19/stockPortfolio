# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: dbconnect.py
# Purpose: Sqlite3 allows us to have an embedded database where we can store login credentials.
# Modification: - Added Users class to store user login info.
# ----------------------------------------------------------------------------------------

from flask import render_template, Flask, redirect, url_for, request, g
from stockPortfolio import app
from flask_sqlalchemy import SQLAlchemy

import sqlite3


# Database path
db = SQLAlchemy(app)
conn = sqlite3.connect("users.db")
c = conn.cursor()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return (self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)


def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(25), password VARCHAR(25), email VARCHAR(50))")

def insertTable(username, password, email):
    insertStatement = "INSERT INTO TABLE {} VALUES({}, {}, {})".format('users', username, password, email)

    c.execute(insertStatement)
    conn.commit()

    c.close()
    conn.close()
