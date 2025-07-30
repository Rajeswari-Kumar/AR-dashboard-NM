import os
import random
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ar-dashboard')
def ar_dashboard():
    try:
        # Dynamic data that changes on each request
        base_sales = 125000
        sales_variation = random.randint(-15000, 25000)
        current_sales = base_sales + sales_variation
        
        growth_rate = round(random.uniform(8.5, 22.3), 1)
        
        regions = ['North', 'South', 'East', 'West']
        regional_data = []
        
        
        for region in regions:
            base_amount = random.randint(25000, 55000)
            regional_data.append({
                'region': region, 
                'sales': base_amount
            })
        
        # Find the top performing region
        top_region = max(regional_data, key=lambda x: x['sales'])
        
        return jsonify({
            'kpis': {
                'total_sales': current_sales,
                'region_leader': top_region['region'],
                'growth_rate': f"{growth_rate}%"
            },
            'regional_data': regional_data,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
