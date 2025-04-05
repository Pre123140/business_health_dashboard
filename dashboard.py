import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Load the cleaned dataset
import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'enhanced_superstore.csv'))
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Calculate Recency, Frequency, and Monetary (RFM) Analysis
snapshot_date = df['Order Date'].max() + pd.DateOffset(days=1)
rfm = df.groupby('Customer ID').agg({
    'Order Date': lambda x: (snapshot_date - x.max()).days,
    'Customer ID': 'count',
    'Sales': 'sum'
}).rename(columns={'Order Date': 'Recency', 'Customer ID': 'Frequency', 'Sales': 'Monetary'})

# Normalize RFM scores
rfm['Recency_Score'] = pd.qcut(rfm['Recency'], q=4, labels=[4, 3, 2, 1]).astype(int)
rfm['Frequency_Score'] = pd.qcut(rfm['Frequency'], q=4, labels=[1, 2, 3, 4]).astype(int)
rfm['Monetary_Score'] = pd.qcut(rfm['Monetary'], q=4, labels=[1, 2, 3, 4]).astype(int)
rfm['RFM_Score'] = rfm[['Recency_Score', 'Frequency_Score', 'Monetary_Score']].sum(axis=1)

# Segment customers based on RFM Score
rfm['Segment'] = rfm['RFM_Score'].apply(lambda x: 'Champions' if x >= 10 else ('Loyal' if x >= 8 else ('Potential' if x >= 6 else 'Needs Attention')))

# RFM Segmentation Pie Chart
fig_rfm_segments = px.pie(rfm, names='Segment', title='🔍 Customer Segmentation Based on RFM Analysis')

# Initialize the Dash app
app = dash.Dash(__name__)

# Sales Trend Plot
sales_trend = df.groupby(df['Order Date'].astype(str))['Sales'].sum().reset_index()
fig_sales_trend = px.line(sales_trend, x='Order Date', y='Sales', title='📈 Monthly Sales Trend')

# Sales by Category Plot
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
fig_sales_category = px.bar(sales_by_category, x='Category', y='Sales', title='💰 Sales by Category', color='Category')

# Top Customers Plot
top_customers = df.groupby('Customer ID').agg({'Sales': 'sum'}).sort_values(by='Sales', ascending=False).head(10).reset_index()
fig_top_customers = px.bar(top_customers, x='Customer ID', y='Sales', title='🏆 Top 10 Customers by Sales', color='Sales')

# Customer Segmentation Pie Chart (Fix applied here)
segment_counts = df['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'count']  # Rename columns
fig_customer_segments = px.pie(segment_counts, names='Segment', values='count', title='👥 Customer Segmentation')

# Sales & Profit Trend Plot
monthly_financials = df.groupby(df['Order Date'].astype(str)).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
fig_financial_trend = go.Figure()
fig_financial_trend.add_trace(go.Scatter(x=monthly_financials['Order Date'], y=monthly_financials['Sales'], mode='lines+markers', name='Sales'))
fig_financial_trend.add_trace(go.Scatter(x=monthly_financials['Order Date'], y=monthly_financials['Profit'], mode='lines+markers', name='Profit'))
fig_financial_trend.update_layout(title='📈 Monthly Sales & Profit Trends', xaxis_title='Month', yaxis_title='Amount ($)')

# Discount vs Profit Scatter Plot
fig_discount_profit = px.scatter(df, x='Discount', y='Profit', title='💡 Impact of Discount on Profit', opacity=0.6)

# Layout of the Dashboard
app.layout = html.Div([
    html.H1("Business Performance Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(figure=fig_sales_trend),
        dcc.Graph(figure=fig_sales_category)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    
    html.Div([
        dcc.Graph(figure=fig_top_customers),
        dcc.Graph(figure=fig_customer_segments)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    
    html.Div([
        dcc.Graph(figure=fig_financial_trend),
        dcc.Graph(figure=fig_discount_profit)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    
    html.Div([
        dcc.Graph(figure=fig_rfm_segments)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
