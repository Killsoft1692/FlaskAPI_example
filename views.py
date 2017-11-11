from main import app, db, request, status
from models import Product


@app.route('/', methods=['GET'])
def get_products():
    response = []
    products = db.session.query(Product).all()
    for product in products:
        values = dict()
        values['id'] = product.id
        values['name'] = product.name
        values['price'] = product.price
        response.append(values)

    return response


@app.route('/product/<pk>', methods=['GET'])
def get_product(pk):
    product = db.session.query(Product).get(int(pk))
    if product:

        return {
            "name": product.name,
            "price": product.price,
            "available": product.in_stock
        }, status.HTTP_200_OK
    else:

        return '', status.HTTP_404_NOT_FOUND


@app.route('/product/<pk>', methods=['PATCH'])
def update_product(pk):
    product = db.session.query(Product).get(int(pk))
    if product:
        product.name = request.data.get('name')
        product.price = request.data.get('price')
        product.in_stock = request.data.get('in_stock')
        db.session.add(product)
        db.session.commit()

        return {
            "name": product.name,
            "price": product.price,
            "available": product.in_stock
        }, status.HTTP_200_OK
    else:

        return '', status.HTTP_404_NOT_FOUND


@app.route('/product/<pk>', methods=['DELETE'])
def delete_product(pk):
    product = db.session.query(Product).get(int(pk))
    if product:
        db.session.delete(product)

        return '', status.HTTP_200_OK
    else:

        return '', status.HTTP_404_NOT_FOUND


@app.route('/create_products', methods=['POST'])
def set_products():
    for item in request.data:
        product = Product(
            name=item.get('name'),
            price=item.get('price'),
            in_stock=item.get('in_stock')
        )
        db.session.add(product)
    db.session.commit()

    return '', status.HTTP_201_CREATED
