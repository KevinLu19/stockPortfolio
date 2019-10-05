# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/30/2019
# File: app.py
# Purpose: Runs application.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from stockPortfolio import app  # Imports __init__ file. init file contains app (have to be in there)

if __name__ == "__main__":
    app.run(debug=True)