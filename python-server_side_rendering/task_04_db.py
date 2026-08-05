from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_file(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['price'] = float(row['price'])
                except ValueError:
                    pass
                products.append(row)
    except Exception:
        return []
    return products

def read_sqlite_db(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception:
        return []
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter including 'sql'
    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    elif source == 'sql':
        data = read_sqlite_db('products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter by id if provided
    if product_id is not None:
        filtered_data = [p for p in data if str(p.get('id')) == str(product_id)]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
