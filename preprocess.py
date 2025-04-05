import pandas as pd

def load_clean_data():
    try:
        file_path = "data/superstore.csv"
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Convert Date Columns to Datetime Format
        df["Order Date"] = pd.to_datetime(df["Order Date"])
        df["Ship Date"] = pd.to_datetime(df["Ship Date"])

        # Create Shipping Duration
        df["Shipping Duration"] = (df["Ship Date"] - df["Order Date"]).dt.days

        # Extract Date Features
        df["Order Year"] = df["Order Date"].dt.year
        df["Order Month"] = df["Order Date"].dt.month
        df["Order Day"] = df["Order Date"].dt.day
        df["Order Weekday"] = df["Order Date"].dt.day_name()

        # Drop Unnecessary Columns
        df.drop(["Row ID", "Customer Name", "Country"], axis=1, inplace=True)

        # Print Column Names After Processing
        print("\n✅ Data Preprocessed Successfully!")
        print("🔹 Columns after preprocessing:\n", df.columns)

        return df

    except Exception as e:
        print("❌ Error in preprocessing:", e)
        return None

# Run the function to test
if __name__ == "__main__":
    load_clean_data()
