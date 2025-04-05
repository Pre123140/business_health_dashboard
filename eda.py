import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda():
    try:
        # Load preprocessed data
        file_path = "data/superstore.csv"
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Convert Order Date to datetime
        df["Order Date"] = pd.to_datetime(df["Order Date"])

        # Summary Statistics
        print("\n🔍 Basic Summary:")
        print(df.describe())

        # Sales Trend Over Time
        plt.figure(figsize=(12, 6))
        df.groupby("Order Date")["Sales"].sum().plot()
        plt.title("📊 Sales Trend Over Time")
        plt.xlabel("Order Date")
        plt.ylabel("Total Sales")
        plt.grid()
        plt.show()

        # Top Categories by Sales
        plt.figure(figsize=(10, 5))
        sns.barplot(x=df.groupby("Category")["Sales"].sum().index, 
                    y=df.groupby("Category")["Sales"].sum().values)
        plt.title("🏆 Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.show()

        print("\n✅ EDA Completed Successfully!")

    except Exception as e:
        print("❌ Error in EDA:", e)

# Run the function to test
if __name__ == "__main__":
    perform_eda()
