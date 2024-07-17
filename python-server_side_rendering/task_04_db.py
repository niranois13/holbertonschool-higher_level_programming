from flask import Flask, render_template, request
import json
import os
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(items_file_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)

    items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error_message = None

    if source == 'db':
        product_db_file_path = os.path.join(os.path.dirname(__file__), 'products.db')
        if not os.path.exists(product_db_file_path):
            error_message = 'Database not found'

        else:
            try:
                conn = sqlite3.connect(product_db_file_path)
                cursor = conn.cursor()
                if product_id:
                    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
                    products = cursor.fetchall()
                else:
                    cursor.execute('SELECT * FROM products')
                    products = cursor.fetchall()
                conn.close()
                products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
            except sqlite3.Error as e:
                return render_template('products.html', error=f'Database error: {str(e)}')

    elif source == 'json':
        product_json_file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        with open(product_json_file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                products = data
            else:
                products = data.get('products', dict)

    elif source == 'csv':
        product_csv_file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        with open(product_csv_file_path, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)

    else:
        error_message = "Wrong source"

    if product_id and not error_message:
        products = [product for product in products if str(product.get('id')) == str(product_id)]

    return render_template('products.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
