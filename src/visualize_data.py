import matplotlib.pyplot as plt

#Chart 1:Regional Sales
def plot_sales_by_region(df):

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Region"],
        df["TotalSales"]
    )

    plt.title(
        "Sales by Region"
    )

    plt.xlabel(
        "Region"
    )

    plt.ylabel(
        "Revenue ($)"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/sales_by_region.png"
    )

    plt.close()

#Chart 2:Top Products
def plot_top_products(df):

    plt.figure(figsize=(10, 6))

    plt.barh(
        df["Product Name"],
        df["Revenue"]
    )

    plt.title(
        "Top 10 Products by Revenue"
    )

    plt.xlabel(
        "Revenue ($)"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/top_products.png"
    )

    plt.close()

#Chart 3:Category Profit
def plot_profit_by_category(df):

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Category"],
        df["TotalProfit"]
    )

    plt.title(
        "Profit by Category"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Profit ($)"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/profit_by_category.png"
    )

    plt.close()

#Chart 4:Top Customers
def plot_top_customers(df):

    plt.figure(figsize=(10, 6))

    plt.barh(
        df["Customer Name"],
        df["Revenue"]
    )

    plt.title(
        "Top 10 Customers by Revenue"
    )

    plt.xlabel(
        "Revenue ($)"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/top_customers.png"
    )

    plt.close()

#Chart 6:Discount vs Profit
def plot_discount_vs_profit(df):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["Discount"],
        df["Profit"],
        alpha=0.3
    )

    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit ($)")
    plt.axhline(0, color="red", linewidth=0.8, linestyle="--")
    plt.tight_layout()
    plt.savefig("outputs/discount_vs_profit.png")
    plt.close()

#Chart 7:YoY Growth
def plot_yoy_growth(df):

    df["YoY_Growth"] = df["TotalSales"].pct_change() * 100

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Year"],
        df["YoY_Growth"],
        color=["green" if x >= 0 else "red" for x in df["YoY_Growth"]]
    )

    plt.title("Year-over-Year Sales Growth (%)")
    plt.xlabel("Year")
    plt.ylabel("Growth (%)")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.tight_layout()
    plt.savefig("outputs/yoy_growth.png")
    plt.close()

#Chart 8:KPI Summary
def plot_kpi_summary(df):

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    kpis = [
        ("Total Revenue", f"${df['TotalRevenue'][0]:,.0f}"),
        ("Total Profit", f"${df['TotalProfit'][0]:,.0f}"),
        ("Total Orders", f"{df['TotalOrders'][0]:,}")
    ]

    for ax, (label, value) in zip(axes, kpis):
        ax.text(0.5, 0.5, value, ha="center", va="center", fontsize=24, fontweight="bold")
        ax.text(0.5, 0.2, label, ha="center", va="center", fontsize=12, color="gray")
        ax.axis("off")

    plt.suptitle("KPI Summary", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("outputs/kpi_summary.png")
    plt.close()

def plot_monthly_sales(df):

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["Month"],
        df["Revenue"]
    )

    plt.title(
        "Monthly Sales Trend"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Revenue ($)"
    )

    biannual_ticks = [i for i, m in enumerate(df["Month"]) if m.endswith("-01") or m.endswith("-07")]
    plt.xticks(ticks=biannual_ticks, labels=[df["Month"].iloc[i] for i in biannual_ticks], rotation=45)

    plt.tight_layout()

    plt.savefig(
        "outputs/monthly_sales_trend.png"
    )

    plt.close()