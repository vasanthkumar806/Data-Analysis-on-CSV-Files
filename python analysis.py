import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df.head()
df.info()
df.describe()

category_sales = df.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
top_products.plot(kind="bar")
plt.title("Top 5 Best-Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

category_sales.to_csv("category_sales_summary.csv")
monthly_sales.to_csv("monthly_sales_summary.csv")
