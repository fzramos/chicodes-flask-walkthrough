# Import the app variable from the init
from chicodes_blog_app import app, db

# Import  specific packages from flask
from flask import render_template, request, redirect, url_for

# Import user created form class
from chicodes_blog_app.forms import UserInfoForm, LoginForm, PostForm

# Import of Our model(s) for the Database
from chicodes_blog_app.models import User, Post, check_password_hash

#Import for Flask Login functions - login_required
# login_user, current_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user

# Default Home route
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', user_posts = posts)

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
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # This is basically a sql SELECT STATEMENT
        # SELECT * FROM user WHERE User.email == email LIMIT 1

        # check the password of the newly found user
        # and validate the password against the hash value 
        # inside fo the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # TODO redirect user 
            # doing redirect
            return redirect(url_for('home'))
        else:
            # return 'Not Logged in'
            # TODO redirect user to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # feature inside of flask_login library
    return redirect(url_for('home'))

# Creation of posts route
@app.route('/posts', methods = ['GET', 'POST'])
@login_required
def posts():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id

        post = Post(title, content, user_id)
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('posts.html', post_form = form)

# post detail route to dsiplay info about a post
@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post)

# UPDATE post
@app.route('/posts/update/<int:post_id>', methods=["GET", "POST"])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()

    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id

        # Update the database with new info at that post id
        post.title = title
        post.content = content
        post.user_id = user_id

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post_update.html', update_form = form)

# DELETE post
@app.route('/posts/delete/<int:post_id>', methods = ['GET', 'POST', 'DELETE'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

