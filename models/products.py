from app import db
from flask_bcrypt import Bcrypt as bcrypt

#users model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def insert_record(self):
        db.session.add(self)
        db.session.commit()

    # check if email is in use
    @classmethod
    def check_email_exist(cls, email):
        owners = cls.query.filter_by(email=email).first()
        db.session.close()
        if owners:
            return True
        else:
            return False

    # validate password
    @classmethod
    def validate_password(cls, email, password):
        owners = cls.query.filter_by(email=email).first()
        passwordcheck = bcrypt.check_password_hash(owners.password, password)
        db.session.close()
        if owners and passwordcheck:
            return True            
        else:
            return False

    # get customer id
    @classmethod
    def get_user_by_email(cls, email):
        user = cls.query.filter_by(email=email).first().id
        db.session.close()
        return user

#product model
class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(),nullable=False,primary_key=True)
    product = db.Column(db.String(),nullable=False)
    category = db.Column(db.String(),nullable=False)
    description = db.Column(db.String(),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    breakages = db.Column(db.Integer,nullable=False)


    def create_product(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def low_stock(cls,lowest):
    #     lowstock = cls.query.filter_by(quantity = lowest)
    #     return lowstock

    @classmethod
    def all_products(cls):
        products = cls.query.all()
        db.session.close()
        return products


    @classmethod
    def product_by_category(cls,category):
        products = cls.query.filter_by(category = category)
        db.session.close()
        if products:
            return products
        else:
            return False


    @classmethod
    def get_product_by_name(cls,name):
        product = cls.query.filter_by(product=name).first()
        db.session.close()
        if product:
            return product
        else:
            return False


    @classmethod
    def get_product_by_stock_size(cls,criteria):
        if criteria:
            products = cls.query.all().order_by()
            db.session.close()
            return products
        else:
            return False


    @classmethod
    def update_quantity_by_product_id(cls,id,quantity):
        updateProduct = cls.query.filter_by(id=id).first()
        db.session.close()
        if updateProduct:
            updateProduct.quantity = quantity
            db.session.commit()
            db.session.close()
            return True
        else:
            return False


    @classmethod
    def delete_available_product_by_id(cls,id):
        product = cls.query.filter_by(id = id).first()
        db.session.close()
        if product:
            product.delete()
            db.session.close()
            return True
        else:
            return False

class RestockRequest(db.Model):
    __tablename__ = 'restockrequests'
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    product = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    status = db.Column(db.String(),nullable=False)


    def create_product(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()

    @classmethod
    def all_request(cls):
        requests = cls.query.all()
        db.session.close()
        return requests
    


class Warehouse(db.Model):
    __tablename__ = 'warehouses'
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    type = db.Column(db.String(200))