import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
try:
    df = pd.read_csv('data/enhanced_superstore.csv')
    print("✅ Data loaded successfully for Financial Analysis!")
except FileNotFoundError:
    print("❌ Error: File 'enhanced_superstore.csv' not found. Please check the file path.")
    exit()

# 💰 Monthly Sales & Profit Trends
df['Order Date'] = pd.to_datetime(df['Order Date'])
monthly_financials = df.groupby(df['Order Date'].dt.to_period("M")).agg({'Sales': 'sum', 'Profit': 'sum'})

# Plot Sales & Profit Trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_financials, x=monthly_financials.index.astype(str), y="Sales", label="Sales", marker="o", color="blue")
sns.lineplot(data=monthly_financials, x=monthly_financials.index.astype(str), y="Profit", label="Profit", marker="o", color="green")
plt.xticks(rotation=45)
plt.title("📈 Monthly Sales & Profit Trends")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.show()

# 💸 Impact of Discount on Profit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.6)
plt.title("💡 Impact of Discount on Profit")
plt.xlabel("Discount (%)")
plt.ylabel("Profit ($)")
plt.show()

# Print Summary
print("\n🔍 Financial Analysis Summary:")
print(df[['Sales', 'Profit', 'Discount']].describe())
