import sqlite3
import pandas as pd

#Query 1:Sales by Region
def sales_by_region():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT Region,
           SUM(Sales) AS TotalSales
    FROM sales
    GROUP BY Region
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result

#Query 2:Top Products
def top_products():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT [Product Name],
           SUM(Sales) AS Revenue
    FROM sales
    GROUP BY [Product Name]
    ORDER BY Revenue DESC
    LIMIT 10
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result

#Query 3:Top Customers
def top_customers():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT [Customer Name],
           SUM(Sales) AS Revenue
    FROM sales
    GROUP BY [Customer Name]
    ORDER BY Revenue DESC
    LIMIT 10
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result

#Query 4:Sales by Category
def sales_by_category():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT Category,
           SUM(Sales) AS Revenue
    FROM sales
    GROUP BY Category
    ORDER BY Revenue DESC
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result

#Query 5:Profit by Category
def profit_by_category():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT Category,
           SUM(Profit) AS TotalProfit
    FROM sales
    GROUP BY Category
    ORDER BY TotalProfit DESC
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result

#Query 7:Discount vs Profit
def discount_vs_profit():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT Discount, Profit
    FROM sales
    """

    result = pd.read_sql_query(query, connection)
    connection.close()
    return result

#Query 8:YoY Growth
def yoy_growth():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT
        substr("Order Date", -4) AS Year,
        SUM(Sales) AS TotalSales
    FROM sales
    GROUP BY Year
    ORDER BY Year
    """

    result = pd.read_sql_query(query, connection)
    connection.close()
    return result

#Query 9:KPI Summary
def kpi_summary():

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    query = """
    SELECT
        ROUND(SUM(Sales), 2) AS TotalRevenue,
        ROUND(SUM(Profit), 2) AS TotalProfit,
        COUNT(DISTINCT [Order ID]) AS TotalOrders
    FROM sales
    """

    result = pd.read_sql_query(query, connection)
    connection.close()
    return result

#Query 6:Monthly Sales
def monthly_sales():
    connection = sqlite3.connect("database/superstore.db")

    query = """
    SELECT
        substr("Order Date", -4) || '-' || printf('%02d', CAST(substr("Order Date", 1, instr("Order Date", '/') - 1) AS INTEGER)) AS Month,
        SUM(Sales) AS Revenue
    FROM sales
    GROUP BY Month
    ORDER BY Month;
    """

    result = pd.read_sql_query(query, connection)
    connection.close()
    return result