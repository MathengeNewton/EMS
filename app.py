from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config.config import *
from models.products import Products  

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run()