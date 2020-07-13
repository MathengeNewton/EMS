from flask import Flask,render_template,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config.config import *

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from models.products import * 
# from models.users import Users

@app.route('/')
def main_page():
    products = Products.all_products()
    return render_template('index.html',products=products)

if __name__ == "__main__":
    app.run()