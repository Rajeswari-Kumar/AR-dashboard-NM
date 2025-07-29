import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_3d_data():
    """Generate 3D visualization data for AR"""
    df = pd.read_csv('sales_data.csv')
    
    # Create 3D bar chart data
    regional_monthly = df.groupby(['region', 'month'])['sales'].sum().reset_index()
    
    bars_data = []
    for _, row in regional_monthly.iterrows():


        bars_data.append({
            'region': row['region'],
            'month': int(row['month']),
            'value': int(row['sales']),
            'height': float(row['sales'] / 1000),  # Scale for AR
            'color': get_region_color(row['region'])
        })
    
    return {
        'bars': bars_data,
        'max_value': int(df['sales'].max()),
        'grid_size': {'x': 4, 'z': 12}  # 4 regions, 12 months
    }

def get_region_color(region):
    """Get color for each region"""
    colors = {
        'North': '#FF6B6B',
        'South': '#4ECDC4', 
        'East': '#45B7D1',
        'West': '#96CEB4'
    }
    return colors.get(region, '#CCCCCC')
