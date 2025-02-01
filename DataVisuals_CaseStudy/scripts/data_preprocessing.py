import pandas as pd
import os
####
import matplotlib.pyplot as plt
import seaborn as sns

# Import Relative Paths
data_path = os.path.abspath('../CaseStudyOstrica/DataVisuals_CaseStudy/data')

# Load Data
sales_df = pd.read_excel(data_path + "/Salesdata_case.xlsx")
customers_df = pd.read_excel(data_path + "/Customerdata_case.xlsx")

# Handle Missing Values
sales_df.dropna(inplace=True)
customers_df.dropna(inplace=True)

# Convert Date Column and Extract Month and Quarter information
sales_df['date'] = pd.to_datetime(sales_df['date'])
sales_df["year_month"] = sales_df["date"].dt.to_period("M")
sales_df["year_quarter"] = sales_df["date"].dt.to_period("Q")

# Merge the DataFrames
sales_df.rename(columns={"customer ID" : "customer_ID"}, inplace=True)
merged_df = pd.merge(sales_df, customers_df, on="customer_ID", how="left")

# Aggregate Sales by Month or Quarter
monthly_sales = merged_df.groupby("year_month")["total_price"].sum().reset_index()
quarterly_sales = merged_df.groupby("year_quarter")["total_price"].sum().reset_index()

# Handle Missing Months
all_months = pd.date_range(start=merged_df["date"].min(), end=merged_df["date"].max(), freq="ME").to_period("M")
monthly_sales = monthly_sales.set_index("year_month").reindex(all_months, fill_value=0).reset_index()
monthly_sales.rename(columns={"index" : "year_month"}, inplace=True)

# Assign Sales Manager
emma_cities = ["Amsterdam", "'s-Gravenhage", "'s-Hertogenbosch", "Delft"]

def assign_sales_manager(city):
    if city in emma_cities:
        return "Emma"
    return "Max"

merged_df["sales_manager"] = merged_df["city"].apply(assign_sales_manager)

# Aggregate Sales by Manager
manager_sales = merged_df.groupby("sales_manager")["total_price"].sum().reset_index()

# Save the Cleaned Data
merged_df.to_excel(data_path + "/cleaned_data.xlsx", index=False, engine="openpyxl")

#########
## visualisation with matplotlib & Seaborn

# Convert Period to String Before Plotting
monthly_sales["year_month"] = monthly_sales["year_month"].astype(str)
quarterly_sales["year_quarter"] = quarterly_sales["year_quarter"].astype(str)

"""

## Plot Monthly Sales Trend
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x="year_month", y="total_price", marker="o", linewidth=2)
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

## Plot Quarterly Sales Trend
plt.figure(figsize=(8, 5))
sns.lineplot(data=quarterly_sales, x="year_quarter", y="total_price", palette="coolwarm")
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.grid(axis="y")
plt.show()

"""
