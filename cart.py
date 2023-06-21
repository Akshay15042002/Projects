from flask import Flask, render_template

app = Flask(__name__)

# Product data
products = [
    {'Shirt': 'Product 1', 'price': 10.99},
    {'Pant': 'Product 2', 'price': 19.99},
    {'name': 'Product 3', 'price': 7.99},
    # Add more products as needed
]


# Cart to store selected items
cart = []

# Route to display products and handle cart operations
@app.route('/', methods=['GET', 'POST'])
def handle_cart():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            cart.append(product)
            message = f"Added {product['name']} to the cart!"
        else:
            message = "Product not found."
        return render_template('index.html', products=products, cart=cart, message=message)
    else:
        return render_template('index.html', products=products, cart=cart)

# Calculate the total cost of items in the cart
def calculate_total_cost():
    total_cost = sum(product['price'] for product in cart)
    return total_cost

# Route to display the cart and total cost
@app.route('/cart')
def display_cart():
    total_cost = calculate_total_cost()
    return render_template('cart.html', cart=cart, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
