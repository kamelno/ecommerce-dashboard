import pandas as pd
import numpy as np

class EcommerceAnalytics:
    def __init__(self):
        self.categories = ['Electronics', 'Fashion', 'Home', 'Beauty']
        
    def generate_mock_data(self, n_rows=10):
        """توليد بيانات وهمية لحظية لمحاكاة الواقع"""
        data = {
            'order_id': np.arange(1000, 1000 + n_rows),
            'product': np.random.choice(['Laptop', 'iPhone', 'Hoodie', 'Watch', 'Sneakers'], n_rows),
            'category': np.random.choice(self.categories, n_rows),
            'price': np.random.uniform(50, 2000, n_rows).round(2),
            'timestamp': pd.Timestamp.now()
        }
        return pd.DataFrame(data)

    def calculate_kpis(self, df):
        """حساب المؤشرات الرئيسية للأداء"""
        total_revenue = df['price'].sum()
        total_orders = len(df)
        avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
        return total_revenue, total_orders, avg_order_value