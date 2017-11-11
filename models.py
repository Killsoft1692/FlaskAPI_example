from main import db


class Product(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(length=256))
    price = db.Column(db.FLOAT)
    in_stock = db.Column(db.BOOLEAN)

    def __repr__(self):
        return self.name+'=>'+self.price
