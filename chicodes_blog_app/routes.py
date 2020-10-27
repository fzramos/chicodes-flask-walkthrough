# Import the app variable from the init
from chicodes_blog_app import app

# Import  specific packages from flask
from flask import render_template

# Import user created form class
from chicodes_blog_app.forms import UserInfoForm

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
    return render_template('register.html', user_form = form)
    # user_form is just variable name, nothing special, not keywork