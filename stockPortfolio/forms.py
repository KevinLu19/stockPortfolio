# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/5/2019
# File: forms.py
# Purpose: Creating python version of Login and Register html using WTForms and python classes.
# Modification: - Added LoginForm
# ----------------------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from stockPortfolio.models import User

class RegisterationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=25)])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password"),Length(min=5, max=15)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    submit = SubmitField("Sign Up")

    # Check if username already exist in database.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if (user):
            raise (ValidationError("Username has already been taken. Please choose a different one!"))
    
    # Check if email already exist in database.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if (user):
            raise (ValidationError("Email has already been taken. Please choose a different one!"))

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=25)])

    submit = SubmitField("Log In")