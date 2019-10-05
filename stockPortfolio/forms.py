# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/5/2019
# File: forms.py
# Purpose: Creating python version of Login and Register html using WTForms and python classes.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=25)])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password"),Length(min=5, max=15)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=25)])

    submit = SubmitField("Log In")