import sqlite3
conn = sqlite3.connect("database/superstore.db")
cur = conn.execute("SELECT DISTINCT substr(\"Order Date\", 7, 4) || '-' || substr(\"Order Date\", 1, 2) AS Month FROM sales ORDER BY Month")
print([r[0] for r in cur.fetchall()])
conn.close()