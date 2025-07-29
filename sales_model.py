import pandas as pd
import numpy as np

def get_regional_data():
    """Get regional performance for AR visualization"""
    df = pd.read_csv('sales_data.csv')
    regional_stats = df.groupby('region').agg({
        'sales': ['sum', 'mean', 'count']
    }).round(2)
    
    return {
        region: {
            'total_sales': int(stats[('sales', 'sum')]),

            'avg_sales': float(stats[('sales', 'mean')]),
            'transactions': int(stats[('sales', 'count')]),
            'position': get_ar_position(region)
        }
        for region, stats in regional_stats.iterrows()
    }

def get_trend_data():
    """Get monthly trends for AR timeline"""
    df = pd.read_csv('sales_data.csv')
    monthly_trends = df.groupby('month')['sales'].sum().to_dict()
    return {str(k): int(v) for k, v in monthly_trends.items()}

def get_ar_position(region):
    """Map regions to AR world positions"""
    positions = {
        'North': {'x': 0, 'y': 1, 'z': 2},
        'South': {'x': 0, 'y': 1, 'z': -2},
        'East': {'x': 2, 'y': 1, 'z': 0},
        'West': {'x': -2, 'y': 1, 'z': 0}
    }
    return positions.get(region, {'x': 0, 'y': 1, 'z': 0})

def get_kpis():
    """Get key performance indicators for dashboard"""
    df = pd.read_csv('sales_data.csv')
    
    total_sales = int(df['sales'].sum())
    regional_totals = df.groupby('region')['sales'].sum()
    region_leader = regional_totals.idxmax()
    
    
    # Calculate growth rate (mock calculation)
    current_month = df[df['month'] == df['month'].max()]['sales'].sum()
    prev_month = df[df['month'] == df['month'].max() - 1]['sales'].sum()
    growth_rate = f"{((current_month - prev_month) / prev_month * 100):.1f}%"
    
    return {
        'total_sales': total_sales,
        'region_leader': region_leader,
        'growth_rate': growth_rate
    }
