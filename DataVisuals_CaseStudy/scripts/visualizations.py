import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



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

