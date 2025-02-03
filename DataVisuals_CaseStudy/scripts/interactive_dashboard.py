import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from data_preprocessing import preprocessing

customer_df, sales_df, quarterly_sales, monthly_sales, manager_sales, merged_df = preprocessing()

# Streamlit UI
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("DataVisuals Inc. Dashboard")
st.write("Analize key sales metrics interactively.")

# **Filters**
st.sidebar.header("Filters")

# Date Range Filter
start_date = merged_df["date"].min().to_pydatetime()
end_date = merged_df["date"].max().to_pydatetime()
start_date, end_date = st.sidebar.slider(
                                "Select Date Range:",
                                 min_value= start_date,
                                 max_value= end_date,
                                 value=(start_date, end_date),
                                 )

# Sales Manager Dropdown
sales_manager_filter = st.sidebar.selectbox("Filter by Sales Manager:", ["All", "Emma", "Max"])

# City Dropdown (Multi-Select)
city_filter = st.sidebar.multiselect("Filter by City", options=merged_df["city"].unique(), default=merged_df["city"].unique())

# Apply Filters
filtered_sales = merged_df[(merged_df["date"] >= start_date) & (merged_df["date"] <= end_date)]
if sales_manager_filter != "All":
    filtered_sales = filtered_sales[merged_df["sales_manager"] == sales_manager_filter]
if city_filter:
    filtered_sales = filtered_sales[merged_df["city"].isin(city_filter)]

# Show KPI Metrics
st.subheader("Key Performance Indicators Metrics")
total_sales = filtered_sales["total_price"].sum()
average_order_value = filtered_sales["total_price"].mean()
num_transactions = filtered_sales.shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"€{total_sales:,.2f}")
col2.metric("Average Order Value", f"€{average_order_value:,.2f}")
col3.metric("Number of Transactions", f"€{num_transactions}")

# Sales Trend (Monthly)
st.subheader("Monthly Sales Trend")

filtered_sales["year_month"] = filtered_sales["year_month"].dt.to_timestamp()
filtered_sales = filtered_sales.set_index("year_month")
monthly_sales = filtered_sales.resample("M")["total_price"].sum().reset_index()

fig_monthly_trend = px.line(monthly_sales, 
               x="year_month", 
               y="total_price", 
               markers=True, 
            #    title="Monthly Sales Trend",
               )

fig_monthly_trend.update_layout(
    xaxis_title="Date",
    yaxis_title="ToTal Price",
)

st.plotly_chart(fig_monthly_trend, use_container_width=True)

# Revenue by Sales Manager
st.subheader("Revenue per Sales Manager")

sales_manager_revenue = filtered_sales.groupby("sales_manager")["total_price"].sum().reset_index()

fig2 = px.bar(
    sales_manager_revenue, 
    x="sales_manager", 
    y="total_price", 
    # title="Revenue per Sales Manager", 
    color="sales_manager"
    )

fig2.update_layout(
    xaxis_title="Sales Manager",
    yaxis_title="ToTal Price",
)

st.plotly_chart(fig2, use_container_width=True)


# Cities by Sales
st.subheader("Cities by Sales")

cities = filtered_sales.groupby("city")["total_price"].sum().reset_index().sort_values(by="total_price", ascending=False)

fig3 = px.bar(
    cities,
    x="city",
    y="total_price",
    # title="Cities by Sales",
    color="city"
)

fig3.update_layout(
    xaxis_title="City",
    yaxis_title="ToTal Price",
)

st.plotly_chart(fig3, use_container_width=True)

##### Top Cities by Sales
# top_cities = filtered_sales.groupby("city")["total_price"].sum().reset_index().sort_values(by="total_price", ascending=False).head(5)

# fig4 = px.bar(
#     top_cities,
#     x="city",
#     y="total_price",
#     title="Top Cities by Sales",
#     color="city"
# )

# fig4.update_layout(
#     xaxis_title="City",
#     yaxis_title="ToTal Price",
# )

# st.plotly_chart(fig4, use_container_width=True)


#### Newsletter opt-in
st.subheader("Newsletter Opt-in Rate")

# Count opt-ins 
newsletter_counts = merged_df["newsletter"].value_counts().reset_index()
newsletter_counts.columns = ["Opt-in Status", "Count"]

# Interactive Pie Chart
fig4 = px.pie(newsletter_counts, names="Opt-in Status", values="Count", 
                #    title="Newsletter Opt-in Rate", 
                   color_discrete_sequence=["#66c2a5", "#fc8d62"])
st.plotly_chart(fig4)


st.subheader("Customer Order Frequency")

customer_order_counts = merged_df["customer_ID"].value_counts()
order_count_distribution = customer_order_counts.reset_index()
order_count_distribution.columns = ["Orders Made", "Number of Customers"]

fig5 = px.bar(order_count_distribution, 
              x="Orders Made",
              y="Number of Customers", 
              title="Customer Order Frequency Distribution",
              color="Number of Customers",
              color_continuous_scale="blues",
              )
st.plotly_chart(fig5)


# Repeat Customer Rate
st.subheader("Repeat Customer Rate")

repeat_cutomers = customer_order_counts[customer_order_counts > 1].count()
total_customers = merged_df["customer_ID"].nunique()
repeat_cutomers_rate = (repeat_cutomers / total_customers) * 100

st.metric(label="Repeat Customer Rate", value=f"{repeat_cutomers_rate:.2f}%")
