import pandas as pd

def feature_engineering():
    try:
        # Load preprocessed data
        file_path = "data/superstore.csv"
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Convert Order Date to datetime
        df["Order Date"] = pd.to_datetime(df["Order Date"])

        # Calculate Customer Lifetime Value (CLV)
        clv = df.groupby("Customer ID")["Sales"].sum().reset_index()
        clv.rename(columns={"Sales": "Customer Lifetime Value"}, inplace=True)
        df = df.merge(clv, on="Customer ID", how="left")

        # Profit Margin Calculation
        df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

        # RFM Analysis (Recency, Frequency, Monetary)
        latest_date = df["Order Date"].max()
        rfm = df.groupby("Customer ID").agg({
            "Order Date": lambda x: (latest_date - x.max()).days,  # Recency
            "Order ID": "count",  # Frequency
            "Sales": "sum"  # Monetary
        }).reset_index()

        rfm.rename(columns={"Order Date": "Recency", "Order ID": "Frequency", "Sales": "Monetary"}, inplace=True)
        df = df.merge(rfm, on="Customer ID", how="left")

        # Save the enhanced dataset
        df.to_csv("data/enhanced_superstore.csv", index=False)

        print("\n✅ Feature Engineering Completed!")
        print("\n🔹 Columns after feature engineering:", df.columns)

    except Exception as e:
        print("❌ Error in Feature Engineering:", e)

# Run the function
if __name__ == "__main__":
    feature_engineering()
