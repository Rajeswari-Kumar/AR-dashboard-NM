import os
import json
import csv
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read_csv_data():
    """Read CSV data without pandas"""
    data = []
    with open('sales_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'region': row['region'],
                'month': int(row['month']),
                'sales': int(row['sales'])
            })
    return data

@app.route('/api/ar-dashboard')
def ar_dashboard():
    try:
        data = read_csv_data()
        # Calculate KPIs without pandas
        total_sales = sum(row['sales'] for row in data)
        
        return jsonify({
            'kpis': {'total_sales': total_sales},
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
