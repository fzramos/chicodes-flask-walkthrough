from chicodes_blog_app import app, db, login_manager

# Import all of the Werkzeug Security methods
from werkzeug.security import generate_password_hash, check_password_hash


# Import for DateTime module (This comes from python)
from datetime import datetime

# Import for the Login Manager UserMixin (basically parent class)
from flask_login import UserMixin

# The User class will have
# An id, username, email
# password, post

# Create the current user_manager using the user_login function
# Which is a decorator(used in this class to send info in to the User Model)
# Specifically the User's ID
@login_manager.user_login
def load_user(user_id):
    return User.query.get(int(user_id))


# now creating a SQL table class User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True)
    # lazy means only add post "when you need it"
    # similar to Join statement, only combines two tables when quired, 
    # tables not forever interjoined

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)
        # This line allows us to save password hashes in DB rather
        # than plaintext passwords which is highly unsafe

    def set_password(self, password):
        """
            Grab the password that is pased into the method
            return the hashed version of the password
            which will be stored inside the database
        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    # repeater?
    # purpose is to return a printable version of the object
    def __repr__(self):
        return f'{self.username} has been created with the following email'\
                + f': {self.email}'
    

# Creation of the Post Model
# The Post model will have an
# id, title, content, date_created
# user_id
# This is not form 'GET','POST' but literally letting a user who has an account
# post to the blog
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n'\
                + f'and the content is {self.content}.'
