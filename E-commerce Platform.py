def add_product(product_name, price, quantity):
    product = {'product_name': product_name, 'price': price, 'quantity': quantity}
    return product

def update_price(product, new_price):
    product['price'] = new_price
    return product

def update_quantity(product, quantity_change):
    product['quantity'] += quantity_change
    return product