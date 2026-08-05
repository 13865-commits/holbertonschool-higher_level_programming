from flask import Flask, render_template, request
import json
import csv

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
                # Convert price to float if possible, keep id as string/int
                try:
                    row['price'] = float(row['price'])
                except ValueError:
                    pass
                products.append(row)
    except Exception:
        return []
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
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
