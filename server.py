import os
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ar-dashboard')
def ar_dashboard():
    try:
        # Mock data for AR dashboard
        return jsonify({
            'kpis': {
                'total_sales': 125000,
                'growth_rate': 15.2,
                'active_customers': 1250
            },
            'regional_data': [
                {'region': 'North', 'sales': 45000},
                {'region': 'South', 'sales': 38000},
                {'region': 'East', 'sales': 42000}
            ],
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
