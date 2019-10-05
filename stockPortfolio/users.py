from stockPortfolio import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        # return ('<User %r>' % (self.username))
        return (f"User('{self.username}', '{self.email}')")

    # def __init__(self , username ,password , email):
    #     self.username = username
    #     self.password = password
    #     self.email = email
 
    # Need these 4 functions to allow Flask-login to work.
    # def is_authenticated(self):
    #     return True
 
    # def is_active(self):
    #     return True
 
    # def is_anonymous(self):
    #     return False
 
    # def get_id(self):
    #     return (self.id)
    
    # def getUsername(self):
    #     return (self.username)
    
    # def getPassword(self):
    #     return (self.password)