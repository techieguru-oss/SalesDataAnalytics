from fpdf import FPDF

CHARTS = [
    ("KPI Summary",             "outputs/kpi_summary.png"),
    ("Sales by Region",         "outputs/sales_by_region.png"),
    ("Top 10 Products",         "outputs/top_products.png"),
    ("Top 10 Customers",        "outputs/top_customers.png"),
    ("Profit by Category",      "outputs/profit_by_category.png"),
    ("Monthly Sales Trend",     "outputs/monthly_sales_trend.png"),
    ("Discount vs Profit",      "outputs/discount_vs_profit.png"),
    ("Year-over-Year Growth",   "outputs/yoy_growth.png"),
]

def generate_pdf_report():

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 10, "Superstore Sales Analytics Report", ln=True, align="C")
    pdf.ln(5)

    for title, path in CHARTS:
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 10, title, ln=True)
        pdf.image(path, w=180)
        pdf.ln(5)

    pdf.output("outputs/sales_report.pdf")
    print("PDF report generated: outputs/sales_report.pdf")
