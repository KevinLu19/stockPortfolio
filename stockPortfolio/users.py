from flask_sqlalchemy import SQLAlchemy
from stockPortfolio import app

db = SQLAlchemy(app)

class User():
    # __tablename__ = "users"
    # username = db.Column('username', db.String(20), unique=True , index=True)
    # password = db.Column('password' , db.String(10))
    # email = db.Column('email',db.String(50),unique=True , index=True)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
 
    # Need these 4 functions to allow Flask-login to work.
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return (self.id)
    
    def getUsername(self):
        return (self.username)
    
    def getPassword(self):
        return (self.password)

    def __repr__(self):
        return ('<User %r>' % (self.username))