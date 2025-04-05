import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
try:
    df = pd.read_csv('data/enhanced_superstore.csv')
    print("✅ Data loaded successfully for Sales Analysis!")
except FileNotFoundError:
    print("❌ Error: File 'enhanced_superstore.csv' not found. Please check the file path.")
    exit()

# Sales trends over time
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_trend = df.groupby(df['Order Date'].dt.to_period("M"))['Sales'].sum()

# Plot Sales Trend
plt.figure(figsize=(12, 6))
sales_trend.plot(kind='line', marker='o', color='b')
plt.title("📈 Monthly Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Sales by category
plt.figure(figsize=(8, 5))
sns.barplot(x=df.groupby('Category')['Sales'].sum().index, y=df.groupby('Category')['Sales'].sum().values, palette="viridis")
plt.title("💰 Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Print Summary
print("\n🔍 Sales Analysis Summary:")
print(df[['Sales', 'Profit', 'Discount']].describe())
