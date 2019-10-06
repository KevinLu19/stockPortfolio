# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/5/2019
# File: forms.py
# Purpose: Replacing typical html file and then grab html forms like usual. Replacing that with Python code to simulate it. 
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class EnteringStock(FlaskForm):
    stockTickerName = StringField("Ticker", validators=[DataRequired()])
    stockQuantity = IntegerField("Quantity", validators=[DataRequired()])
    
    buyButton = SubmitField("Buy Stocks")