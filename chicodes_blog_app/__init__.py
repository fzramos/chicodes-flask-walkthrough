from flask import Flask

#  Import config object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate object
from flask_migrate import Migrate

# Import from the Flask Login Module
from flask_login import LoginManager

app = Flask(__name__)
# complete config cycle for our flask app
# and give accesss to our Database(when we have one)
# along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app, db)

# Login Config - Init for the LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Specify what page to load for NON-authenticated users

from chicodes_blog_app import routes, models