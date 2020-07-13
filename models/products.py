from app import db
from flask_bcrypt import Bcrypt as bcrypt

#users model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def insert_record(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def check_email_exist(cls, email):
        customer = cls.query.filter_by(email=email).first()
        if customer:
            return True
        else:
            return False

    
    @classmethod
    def validate_password(cls, email, password):
        customer = cls.query.filter_by(email=email).first()

        if customer and bcrypt.check_password_hash(customer.password, password):
            return True
        else:
            return False

    
    @classmethod
    def get_customer_id(cls, email):
        return cls.query.filter_by(email=email).first().id

#product model
class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    productName = db.Column(db.String(),nullable=False)
    category = db.Column(db.String(),nullable=False)
    description = db.Column(db.String(),nullable=False)
    quantity = db.Column(db.Integer(),nullable=False)
    units = db.Column(db.Integer(),nullable=False)
    breakages = db.Column(db.Integer())


    def create_product(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def all_products(cls):
        return cls.query.all()


    @classmethod
    def product_by_category(cls,category):
        products = cls.query.filter_by(category = category)
        if products:
            return products
        else:
            return False


    @classmethod
    def get_product_by_name(cls,name):
        product = cls.query.filter_by(name=name).first()
        if product:
            return product
        else:
            return False


    @classmethod
    def get_product_by_stock_size(cls,criteria):
        if criteria:
            products = cls.query.filter_by(quantity < criteria)
            return products
        else:
            return False


    @classmethod
    def update_quantity_by_product_id(cls,id,quantity):
        updateProduct = cls.query.filter_by(id=id).first()
        if updateProduct:
            updateProduct.quantity = quantity
            db.session.commit()
            return True
        else:
            return False


    @classmethod
    def delete_available_product_by_id(cls,id):
        product = cls.query.filter_by(id = id).first()
        if product:
            product.delete()
            return True
        else:
            return False
