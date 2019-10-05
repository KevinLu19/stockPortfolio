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
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db" # For SQLAlchemy
db = SQLAlchemy(app)

# Import modules at the bottom to avoid module circulatization.
from stockPortfolio import login     # Importing login.
from stockPortfolio import dbconnect # Importing embedded database.
from stockPortfolio import stockAPI  # Importing alpha_Vantage api.