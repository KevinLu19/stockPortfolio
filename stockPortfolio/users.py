# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/5/2019
# File: users.py
# Purpose: Class for user database. Used for inserting values to the class database.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from stockPortfolio import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        # return ('<User %r>' % (self.username))
        return (f"User('{self.username}', '{self.email}')")