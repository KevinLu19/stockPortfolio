# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: __init__.py
# Purpose: Tells Python that this is part of the package. Useful for distributing code to others.
# Modification: N/A
#               
# ----------------------------------------------------------------------------------------

from flask import Flask
import sqlite3

# Creating an instance for the app.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///stockPortfolio/users.db" # For SQLAlchemy

import stockPortfolio.login     # Importing login.
import stockPortfolio.dbconnect # Importing embedded database.