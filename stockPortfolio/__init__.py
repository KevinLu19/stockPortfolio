# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: __init__.py
# Purpose: Tells Python that this is part of the package. Useful for distributing code to others.
# Modification: N/A
#               
# ----------------------------------------------------------------------------------------

from flask import Flask

# Creating an instance for the app.
app = Flask(__name__)

import stockPortfolio.login     # Importing login.