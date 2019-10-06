# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: __init__.py
# Purpose: Tells Python that this is part of the stockPortfolio/stockPortfolio package. Initialize stockPortfolio subfolder
# Modification: N/A
#               
# ----------------------------------------------------------------------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating an instance for the app.
app = Flask(__name__)
app.config["SECRET_KEY"] = "5f57e339ae37b2ba3a9ae69eebe20cc6f13f649902ff5d8651" # Secret key protect from modifying cookies. Key generated via "Import secrets"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db" # Embedded database.

db = SQLAlchemy(app)    # Creating an database Instance.

# Import modules at the bottom to avoid module circulatization.
from stockPortfolio import login     # Importing login.
from stockPortfolio import stockAPI  # Importing alpha_Vantage api.
from stockPortfolio import forms     # Importing forms (login and register)