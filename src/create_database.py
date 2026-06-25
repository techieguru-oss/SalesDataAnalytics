import sqlite3
def create_database(df):

    connection = sqlite3.connect(
        "database/superstore.db"
    )

    df.to_sql(
        "sales",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(
        "SQLite database created successfully."
    )