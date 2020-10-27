from flask import Flask

#  Import config object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate object
from flask_migrate import Migrate

app = Flask(__name__)
# complete config cycle for our flask app
# and give accesss to our Database(when we have one)
# along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app, db)

from chicodes_blog_app import routes, models