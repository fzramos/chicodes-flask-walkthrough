# Import the app variable from the init
from chicodes_blog_app import app

# Import  specific packages from flask
from flask import render_template, request

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


    # Validate of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(username, email, password)

    return render_template('register.html', user_form = form)
    # user_form is just variable name, nothing special, not keywork

    