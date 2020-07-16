from flask import Flask,render_template,redirect,url_for,session,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config.config import *
from functions.randomid import randomise

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from models.products import * 
# from models.users import Users

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']        
        if Users.check_email_exist(email):
            if Users.validate_password(email=email, password=password):
                session['email'] = email
                session['uid'] = Users.get_user_by_email(email)
                return redirect(url_for('admin'))
            else:
                flash('Invalid login credentials', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Invalid login credentials', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpass = request.form['confirmpass']
        emailcheck = Users.check_email_exist(email)
        if password != confirmpass:
            flash('Passwords dont match', 'danger')
            return redirect(url_for('register'))
        elif emailcheck:
            flash('Email already in use', 'danger')
            return redirect(url_for('register'))
        else:
            hashpassword = bcrypt.generate_password_hash(password, rounds=None).decode('utf-8')
            y = Users(name=name, email=email, password=hashpassword)
            y.insert_record()
            flash('Account successfully created', 'success')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))

@app.route('/')
def main_page():
    # if 'user' in session:
    products = Products.all_products()
    return render_template('index.html',products=products)
    # else:
    #     return redirect(url_for('login'))


@app.route('/addproduct')
def add_product():
    return render_template('upload.html')

@app.route('/productupload',methods=['POST'])
def upload_product():
    if request.method == 'POST':
        product = request.form['productname']
        description = request.form['description']
        category = request.form['category']
        quantity = request.form['quantity']
        breakages = request.form['breakages']
        id = randomise(10)
        prefix = list(category)
        p_id = prefix[0] + id
        try:
            createproduct = Products(id = p_id,product = product,
                    category=category,description = description,quantity = quantity,breakages = breakages)
            createproduct.create_product()
            flash(u'Added succesifully','success')
            return redirect(url_for('add_product'))
        except:
            flash('Error adding product','danger')
            return redirect(url_for('add_product'))
    else:
        flash('Incorect request Method','danger')
        return redirect(url_for('add_product'))


@app.route('/request')
def receive_stock():
    productlist = Products.all_products()
    # print(type(productlist))
    low_stock = []
    for product in productlist:
        if product.quantity < 20:
            low_stock.append(product)
        # print(product.quantity)
    return render_template('restockrequests.html',records=low_stock)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run()