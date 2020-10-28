# Import the app variable from the init
from chicodes_blog_app import app, db

# Import  specific packages from flask
from flask import render_template, request

# Import user created form class
from chicodes_blog_app.forms import UserInfoForm, LoginForm

# Import of Our model(s) for the Database
from chicodes_blog_app.models import User, Post, check_password_hash
# TODO add comments from Joel
# 
# 
from flask_login import login_required, login_user, current_user, logout_user

# Default Home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    names = ['Robert', 'David', 'Bill', 'Jessey']
    return render_template('test.html', list_names = names)

# GET  == Gathering Info
# POST == Sending info
# Create part of CRUD, critical
@app.route('/register', methods = ['GET', 'POST'])
def register():
    # Init our form
    form = UserInfoForm()


    # Validate of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(username, email, password)

        # Creation/Init of our User Class (aka Model)
        user = User(username, email, password)

        # Open a connection to the database
        db.session.add(user) 
        # similar to file open, need to close it 

        # commit all data to the database
        db.session.commit()

    return render_template('register.html', user_form = form)
    # user_form is just variable name, nothing special, not keywork


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate:
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_in = User.query.filter(User.email == email).first()
        # This is basically a sql SELECT STATEMENT
        # SELECT * FROM user WHERE User.email == email LIMIT 1

        # check the password of the newly found user
        # and validate the password against the hash value 
        # inside fo the database
        if logged_user and check_password_has(logged_user.password, password):
            login_user(logged_user)
            # TODO redirect user 
        else:
            # TODO redirect user to login route
            return 'Not Logged in'
    return render_template('login.html', login_form = form)
        