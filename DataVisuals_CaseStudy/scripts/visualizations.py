import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import preprocessing

customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df = preprocessing()

## Plot Monthly Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x="year_month", y="total_price", marker="o", linewidth=2)

plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()


################# Quarterly Sales
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
plt.show()

## Bar chart
# plt.figure(figsize=(8, 5))
# sns.barplot(
#     data=quarterly_sales, 
#     x="year_quarter", 
#     y="total_price", 
#     hue = "year_quarter",
#     palette="coolwarm", 
#     legend=False,
#     )
# plt.title("Quarterly Sales Comparison")
# plt.xlabel("Quarter")
# plt.ylabel("Total Sales")
# plt.grid(axis="y")
# plt.show()


################## Newletter Opt-in Rate
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

plt.show()


########## Revenue per sales manager
#group by sales manager and sum revenue
sales_manager_revenue = merged_df.groupby("sales_manager")["total_price"].sum().reset_index()

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

plt.title("Revenue per Sales Manager")
plt.xlabel("Sales Manager")
plt.ylabel("Total Revenue (€)")
plt.grid(axis="y")

plt.show()


##### Overall Metrics
####
total_sales = sales_df["total_price"].sum()

average_order_value = sales_df["total_price"].mean()

num_transactions = sales_df.shape[0]

# top 5 selling cities
top_cities = merged_df.groupby("city")["total_price"].sum().reset_index()
top_cities = top_cities.sort_values(by="total_price", ascending=False).head(5)

# # bar chart top selling cities
# plt.figure(figsize=(8, 5))
# sns.barplot(
#     data=top_cities, x="total_price", y="city", hue="total_price", palette="coolwarm", legend=False,
# )

# plt.title("Top 5 Cities by Sales")
# plt.xlabel("Total Sales (€)")
# plt.ylabel("City")

# for index, value in enumerate(top_cities["total_price"]):
#     plt.text(index, value + 500, f"€{value:,.0f}%", va="center", fontsize=12)

# plt.show()

# # a quick summary of total sales, aov and transactions
# fig, ax = plt.subplots(figsize=(6, 3))
# ax.axis =("off")

# metrics = [
#     f"Total Sales: €{total_sales:,.2f}",
#     f"Average Order Value: €{average_order_value:,.2f}",
#     f"Number of Transactions: {num_transactions}",
# ]

# for i, metric in enumerate(metrics):
#     ax.text(0.1, 0.8 - i * 0.3, metric, fontsize=12, fontweight="bold")

# plt.show()

