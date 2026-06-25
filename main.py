from src.load_data import load_dataset
from src.create_database import create_database
from src.sql_queries import *
from src.visualize_data import *
from src.generate_report import generate_pdf_report

DATASET = (
    "data/"
    "Sample - Superstore.csv"
)

df = load_dataset(DATASET)

create_database(df)

print("\nSales by Region\n")
print(sales_by_region())

print("\nTop Products\n")
print(top_products())

print("\nTop Customers\n")
print(top_customers())

print("\nSales by Category\n")
print(sales_by_category())

print("\nProfit by Category\n")
print(profit_by_category())

print("\nMonthly Sales Trend\n")

print(monthly_sales().head())

plot_sales_by_region(
    sales_by_region()
)

plot_top_products(
    top_products()
)

plot_profit_by_category(
    profit_by_category()
)

plot_top_customers(
    top_customers()
)

plot_monthly_sales(
    monthly_sales()
)

plot_discount_vs_profit(
    discount_vs_profit()
)

plot_yoy_growth(
    yoy_growth()
)

plot_kpi_summary(
    kpi_summary()
)

generate_pdf_report()

print(
    "\nCharts and PDF report generated successfully."
)