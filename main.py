from fastapi import FastAPI, Response
import pandas as pd

app = FastAPI(title="E-Commerce Analytics API")

@app.get("/")
def home():
    data = {
        'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home', 'Electronics', 'Clothing'],
        'Region': ['North', 'South', 'South', 'East', 'North', 'East', 'West', 'South'],
        'Sales': [12000, 1500, 8500, 3200, 2100, 4500, 15000, 1800],
        'Profit': [2400, 300, 1700, 800, 400, 900, 3000, 350]
    }
    df = pd.DataFrame(data)
    total_sales = int(df['Sales'].sum())
    total_profit = int(df['Profit'].sum())
    
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
                <h1>📊 E-Commerce Operations & Analytics Dashboard</h1>
                <p>Status: <strong>Active & Connected (FastAPI backend)</strong></p>
                <hr>
                <h3>Key Metrics</h3>
                <p>💰 <strong>Total Sales:</strong> ₹ {total_sales:,}</p>
                <p>📈 <strong>Total Profit:</strong> ₹ {total_profit:,}</p>
            </div>
            <div class="card">
                <h3>Transactional Data Preview</h3>
                {df.to_html(index=False)}
            </div>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)