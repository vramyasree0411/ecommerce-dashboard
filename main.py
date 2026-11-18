import random
from fastapi import FastAPI, Response
import pandas as pd

app = FastAPI(title="E-Commerce Analytics API")

# 1. Programmatically generate 5,000 rows of realistic e-commerce data
num_rows = 5000
categories = ['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports']
regions = ['North', 'South', 'East', 'West']

data = {
    'Order_ID': range(1001, 1001 + num_rows),
    'Category': [random.choice(categories) for _ in range(num_rows)],
    'Region': [random.choice(regions) for _ in range(num_rows)],
    'Sales': [random.randint(500, 25000) for _ in range(num_rows)],
    'Profit': [random.randint(50, 5000) for _ in range(num_rows)],
}

df = pd.DataFrame(data)

# 2. Calculate macro metrics across all 5,000 rows
total_sales = int(df['Sales'].sum())
total_profit = int(df['Profit'].sum())
total_orders = len(df)

# Get top 10 rows for clean HTML table preview
preview_df = df.head(10)


@app.get("/")
def home():
  # Build HTML table rows dynamically from the preview subset
  table_rows = ""
  for _, row in preview_df.iterrows():
    table_rows += f"""
        <tr>
            <td>{row['Order_ID']}</td>
            <td>{row['Category']}</td>
            <td>{row['Region']}</td>
            <td>₹{row['Sales']:,}</td>
            <td>₹{row['Profit']:,}</td>
        </tr>
        """

  html_content = f"""
    <html>
    <head>
        <title>E-Commerce Operations Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; padding: 40px; }}
            .card {{ background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
            th, td {{ padding: 12px; border: 1px solid #ddd; text-align: left; }}
            th {{ background-color: #007bff; color: white; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>E-Commerce Operations & Analytics Dashboard</h1>
            <p>Status: <strong>Active & Connected (FastAPI backend analyzing {total_orders:,} orders)</strong></p>
            <hr>
            <h3>Key Metrics (Full Dataset)</h3>
            <p><strong>Total Orders Processed:</strong> {total_orders:,}</p>
            <p><strong>Total Sales:</strong> ₹{total_sales:,}</p>
            <p><strong>Total Profit:</strong> ₹{total_profit:,}</p>
        </div>
        
        <div class="card">
            <h3>Recent Order Preview (Showing first 10 of {total_orders:,} rows)</h3>
            <table>
                <tr>
                    <th>Order ID</th>
                    <th>Category</th>
                    <th>Region</th>
                    <th>Sales</th>
                    <th>Profit</th>
                </tr>
                {table_rows}
            </table>
        </div>
    </body>
    </html>
    """
  return Response(content=html_content, media_type="text/html")
