import os, sys, glob
import pandas as pd
import os
# import numpy as np
####
import matplotlib.pyplot as plt
import seaborn as sns


# Load Data
def load_data(file_name: str) -> str:
    """
    Loads the data files.
    Assumes that the file will be in the data folder.
    Assumes that the file name will be capitalized and snake case.
    Assumes the file is an .xlsx file.

    Args:
        name (str): the name of the file.

    Returns: 
        File: The file to be used for the dataframe.
    """
    # Import Relative Paths
    data_path = os.path.abspath('../CaseStudyOstrica/DataVisuals_CaseStudy/data')
    raw_files = glob.glob(os.path.join(data_path, "*.xlsx"))

    # Check for Parent Folder
    if not os.path.exists(data_path):
        print(f"Error: Data folder '{data_path}' not found.")
        sys.exit(1)

    # Check for Files
    if not raw_files:
        print(f"Error: no raw data files found in '{data_path}'.")
        sys.exit(1)

    # Load Data
    try:
        raw_df = pd.read_excel(data_path + "/" + str(file_name) + "data_case.xlsx")
    except Exception as e:
        print(f"Error during data processing: {e}")

    return raw_df

def handle_missing_values(raw_df : str)->str:
    """
    Removes missing values.

    Args:
        raw_df(str): the name of the raw dataframe to be cleaned.
    """
    dataframe = load_data(raw_df) # Import Data Frame
    dataframe.dropna(inplace=True)  # Handle Missing Values  
    return dataframe

def convert_date():
    """
    Converts date column to datetime.
    Assumes that the file to be cleaned is the sales file.
    """
    sales_df = handle_missing_values("Sales") # Loads data
    sales_df['date'] = pd.to_datetime(sales_df['date'])
    return sales_df

def extract_month_quarter():
    """
    Extracts month and quarter information.
    """
    sales_df = convert_date()
    sales_df["year_month"] = sales_df["date"].dt.to_period("M") # Extract Month information
    sales_df["year_quarter"] = sales_df["date"].dt.to_period("Q") # Extract Quarter information
    return sales_df

def aggregate_month():
    sales_df = extract_month_quarter()
    monthly_sales = sales_df.groupby("year_month")["total_price"].sum().reset_index()
    return monthly_sales

def aggregate_quarter():
    sales_df = extract_month_quarter()
    quarterly_sales = sales_df.groupby("year_quarter")["total_price"].sum().reset_index()
    return quarterly_sales

def handle_missing_months():
    sales_df = extract_month_quarter()
    monthly_sales = aggregate_month()
    all_months = pd.date_range(start=sales_df["date"].min(), end=sales_df["date"].max(), freq="ME").to_period("M")
    monthly_sales = monthly_sales.set_index("year_month").reindex(all_months, fill_value=0).reset_index()
    monthly_sales.rename(columns={"index" : "year_month"}, inplace=True)
    return monthly_sales

def merge_dataframes():
    """
    Merges both dataframes.
    """
    sales_df = handle_missing_values("Sales")
    customers_df = handle_missing_values("Customer")
    convert_date()
    extract_month_quarter()
    sales_df.rename(columns={"customer ID" : "customer_ID"}, inplace=True)
    merged_df = pd.merge(sales_df, customers_df, on="customer_ID", how="left")
    return merged_df

def decide_sales_manager(city : str)->str:
    emma_cities = ["Amsterdam", "'s-Gravenhage", "'s-Hertogenbosch", "Delft"]
    if city in emma_cities:
        return "Emma"
    return "Max"

def assign_sales_manager():
    merged_df = merge_dataframes()
    merged_df["sales_manager"] = merged_df["city"].apply(decide_sales_manager)
    return merged_df

def aggregate_sales_manager():
    merged_df = assign_sales_manager()
    manager_sales = merged_df.groupby("sales_manager")["total_price"].sum().reset_index()
    return manager_sales

def save_clean_data():
    data_path = os.path.abspath('../CaseStudyOstrica/DataVisuals_CaseStudy/data')
    merged_df = assign_sales_manager()
    try:
        merged_df.to_excel(data_path + "/cleaned_data.xlsx", index=False, engine="openpyxl")

    except Exception as e:
        print(f"Error during data processing: {e}")
    
    return "Clean data saved!"

def preprocessing():
    customer_df = handle_missing_values("Customer")
    sales_df = extract_month_quarter()
    quarterly_sales = aggregate_quarter()
    monthly_sales = handle_missing_months()
    manager_sales = aggregate_sales_manager()
    merged_df = assign_sales_manager()

    return customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df
        


customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df = preprocessing()

# print(customer_df)

#Extract Month and Quarter information
# sales_df["year_month"] = sales_df["date"].dt.to_period("M")
# sales_df["year_quarter"] = sales_df["date"].dt.to_period("Q")


# # Merge the DataFrames
# sales_df.rename(columns={"customer ID" : "customer_ID"}, inplace=True)
# merged_df = pd.merge(sales_df, customers_df, on="customer_ID", how="left")

# # Aggregate Sales by Month or Quarter
# monthly_sales = merged_df.groupby("year_month")["total_price"].sum().reset_index()
# quarterly_sales = merged_df.groupby("year_quarter")["total_price"].sum().reset_index()

# Handle Missing Months
# all_months = pd.date_range(start=merged_df["date"].min(), end=merged_df["date"].max(), freq="ME").to_period("M")
# monthly_sales = monthly_sales.set_index("year_month").reindex(all_months, fill_value=0).reset_index()
# monthly_sales.rename(columns={"index" : "year_month"}, inplace=True)

# Assign Sales Manager
# emma_cities = ["Amsterdam", "'s-Gravenhage", "'s-Hertogenbosch", "Delft"]

# def assign_sales_manager(city):
#     emma_cities = ["Amsterdam", "'s-Gravenhage", "'s-Hertogenbosch", "Delft"]

#     if city in emma_cities:
#         return "Emma"
#     return "Max"

# merged_df["sales_manager"] = merged_df["city"].apply(assign_sales_manager)

# Aggregate Sales by Manager
# manager_sales = merged_df.groupby("sales_manager")["total_price"].sum().reset_index()

# Save the Cleaned Data
# try:
#     merged_df.to_excel(data_path + "/cleaned_data.xlsx", index=False, engine="openpyxl")
#     print(f"Saved clean data!")

# except Exception as e:
#     print(f"Error during data processing: {e}")

#########
## visualisation with matplotlib & Seaborn

# Convert Period to String Before Plotting
monthly_sales["year_month"] = monthly_sales["year_month"].astype(str)
quarterly_sales["year_quarter"] = quarterly_sales["year_quarter"].astype(str)



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


