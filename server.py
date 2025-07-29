import os
import pandas as pd
from flask import Flask, jsonify, send_file
from flask_cors import CORS
from sales_model import get_kpis, get_regional_data, get_trend_data
from generate_charts import generate_3d_data
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for Unity WebGL builds

@app.route('/api/ar-dashboard')
def ar_dashboard():
    """Comprehensive AR dashboard data"""
    try:
        return jsonify({
            'kpis': get_kpis(),
            'regional_data': get_regional_data(),
            'trend_data': get_trend_data(),
            'chart_url': '/sales_chart',
            'timestamp': pd.Timestamp.now().isoformat()
        })
    except Exception as e:
        print(f"Error in ar_dashboard: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/api/3d-data')
def get_3d_visualization_data():
    """3D data for AR visualization"""
    
    try:
        return jsonify(generate_3d_data())
    except Exception as e:
        print(f"Error in 3d_data: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
