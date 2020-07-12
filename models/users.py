from app import db
from flask_bcrypt import Bcrypt as bcrypt

class Accounts(db.Models):
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
