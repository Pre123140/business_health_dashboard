import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
try:
    df = pd.read_csv('data/enhanced_superstore.csv')
    print("✅ Data loaded successfully for Customer Analysis!")
except FileNotFoundError:
    print("❌ Error: File 'enhanced_superstore.csv' not found. Please check the file path.")
    exit()

# Top 10 customers by total sales
top_customers = df.groupby('Customer ID').agg({'Sales': 'sum'}).sort_values(by='Sales', ascending=False).head(10)

# Plot Top Customers
plt.figure(figsize=(10, 5))
sns.barplot(x=top_customers.index, y=top_customers['Sales'], palette="coolwarm")
plt.title("🏆 Top 10 Customers by Sales")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Customer Segmentation Analysis
segment_counts = df['Segment'].value_counts()

# Plot Customer Segmentation
plt.figure(figsize=(6, 6))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen'], startangle=140)
plt.title("👥 Customer Segmentation")
plt.show()

# Print Summary
print("\n🔍 Customer Analysis Summary:")
print(df.groupby('Segment')[['Sales', 'Profit']].mean())
