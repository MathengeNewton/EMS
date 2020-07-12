from app import db
#product model
class Products(db.Models):
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