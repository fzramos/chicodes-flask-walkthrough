from flask import Flask

#  Import config object
from config import Config

app = Flask(__name__)
# complete config cycle for our flask app
# and give accesss to our Database(when we have one)
# along with our Secret Key
app.config.from_object(Config)