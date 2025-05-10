# Business Health Dashboard (AI-Augmented)

This project analyzes sales, customer, and financial performance using AI-powered insights and a modular analytical pipeline. Built entirely in Python, it combines traditional data analysis with enhanced business diagnostics to surface the true health of a retail business.

---

## Project Objective
To create an end-to-end solution that ingests transactional business data, transforms it using domain logic, and delivers actionable insights across sales, customer behavior, and financial metrics.

---

## Real-World Business Value
- Identify profitable vs. discount-heavy categories
- Track customer recency and contribution to revenue
- Detect sales anomalies, seasonal trends, and underperforming segments
- Drive better pricing, targeting, and forecasting decisions

---

## Folder Structure
```
BUSINESS_HEALTH_DASHBOARD/
├── app/
│   └── dashboard.py               # Streamlit dashboard app
├── data/
│   ├── superstore.csv            # Raw data
│   └── enhanced_superstore.csv   # Cleaned + engineered data
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_eda.ipynb
│   ├── 3_sales_analysis.ipynb
│   ├── 4_customer_analysis.ipynb
│   └── 5_financial_analysis.ipynb
├── output/                       # (Optional) Exported visuals or reports
├── src/
│   ├── __init__.py
│   ├── preprocess.py             # Data cleaning and base transformation
│   ├── eda.py                    # Exploratory visuals and correlation
│   ├── sales_analysis.py         # KPI logic for orders, revenue, growth
│   ├── customer_analysis.py      # RFM and loyalty-based segmentation
│   └── financial_analysis.py     # Profitability and discount logict
└── requirements.txt              # Dependencies
```

---

## Key Features & Analysis Modules

### Sales KPIs
- Total Orders, Sales, Profit
- Monthly/Yearly Growth
- Category-wise revenue
- Regional breakdowns

### Customer Insights
- RFM Segmentation (Recency, Frequency, Monetary)
- Top customers by revenue
- Churn indicators (e.g., declining frequency)

### Financial Metrics
- Discount vs. Profit correlation
- Profit Margins by product/category
- Achievement % vs. Targets

---

## Visualizations
- Line Charts: Sales trend over time
- Bar Plots: Profit by Region/Category
- Box Plots: Discount impact on profit
- Heatmaps: Correlation matrix (Recency, Spend, Tenure)
- KPI Tiles: Orders, Sales, Profit Margin, Growth %

---

## Tools & Libraries
- pandas – Data loading, transformation
- matplotlib & seaborn – Charts and trends
- plotly – Interactive visualizations
- streamlit – Real-time dashboard

---

## How to Run the Dashboard

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the dashboard
```bash
streamlit run app/dashboard.py
```

> Ensure data is present in the `/data` folder. You can replace with your own transactional CSV following the same schema.

---

## Conceptual Study
Curious about the logic and analytical reasoning behind each module?

[Read the Full Conceptual Study (PDF)](https://github.com/Pre123140/business_health_dashboard/blob/main/BUSINESS%20HEALTH%20DASHBOARD.pdf)

Includes:
- KPI logic explanation
- Segment scoring frameworks (RFM)
- Strategic takeaways
- Business questions answered through the dashboard

---

## Future Enhancements
- Add predictive analytics (e.g., customer churn, inventory forecasting)
- Connect to live SQL / ERP systems for real-time dashboarding
- Embed anomaly detection for profit drops or demand surges
- Add CSV export per dashboard module

---

## License

This project is open for educational use only. For commercial deployment, contact the author.

---

## Contact
If you'd like to learn more or collaborate on projects or other initiatives, feel free to connect on [LinkedIn](https://www.linkedin.com/in/prerna-burande-99678a1bb/) or check out my [portfolio site](https://youtheleader.com/).

