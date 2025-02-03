import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import preprocessing

customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df = preprocessing()

## Plot Monthly Sales Trend
def plot_monthly_sales():
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x="year_month", y="total_price", marker="o", linewidth=2)

    plt.xticks(rotation=45)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    # return plt.show()
    return plt


## Quarterly Sales
def plot_quarterly_sales():
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=quarterly_sales, 
        x="year_quarter", 
        y="total_price", 
        marker="o", 
        linewidth=2,
        )
    plt.title("Quarterly Sales Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Total Sales")
    plt.grid(axis="y")
    return plt


## Newletter Opt-in Rate
def plot_newsletter_opt_in_rate():
    # calculate opt-in percentage
    total_customers = customer_df.shape[0]
    opt_in_count = customer_df[customer_df["newsletter"] == "Y"].shape[0]
    opt_in_percentage = (opt_in_count / total_customers) * 100

    # Create DataFrame for visualization
    optin_data = pd.DataFrame({
        "Category" : ["Actual Opt-in Rate", "Target Opt-in Rate"],
        "Percentage": [opt_in_percentage, 65]
    })

    # Plot Bar Chart
    plt.figure(figsize=(6, 4))
    sns.barplot(
        data=optin_data, 
        x="Category", 
        y="Percentage", 
        hue="Category", 
        palette=["blue", "red"],
        legend=False,
        )

    # Labels
    plt.title("Newsletter Opt-in Rate vs Target")
    plt.ylabel("Percentage")
    plt.ylim(0, 100)

    # show values on bars
    for index, value in enumerate(optin_data["Percentage"]):
        plt.text(index, value + 2, f"{value:.1f}%", ha="center", fontsize=12)

    return plt


## Revenue per sales manager
def sales_manager_revenue_2023():

    df_2023 = merged_df[merged_df['year_month'].dt.year == 2023]
    # Group by sales manager and sum revenue
    sales_manager_revenue = df_2023.groupby("sales_manager")["total_price"].sum().reset_index()

    # Create bar plot
    sns.barplot(
        data=sales_manager_revenue, 
        x="sales_manager", 
        y="total_price", 
        hue="sales_manager", 
        palette=["blue", "red"],
        legend=False,
        )

    for index, value in enumerate(sales_manager_revenue["total_price"]):
        plt.text(index, value + 500, f"€{value:,.0f}%", ha="center", fontsize=12)

    plt.title("Revenue per Sales Manager in 2023")
    plt.xlabel("Sales Manager")
    plt.ylabel("Total Revenue (€)")
    plt.grid(axis="y")

    return plt