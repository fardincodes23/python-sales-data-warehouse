import sqlite3
import pandas as pd
from transform_data import transform_data

def load_to_database():
    print("Starting the Load process...")

    # 1. Grab the clean DataFrame directly from your previous script
    df = transform_data('raw_sales_data.csv')

    # 2. Connect to a local SQLite database (this creates the file if it doesn't exist)
    conn = sqlite3.connect('sales_warehouse.db')
    cursor = conn.cursor()

    # 3. Define the SQL Schema
    # In Data Engineering, transactional tables are often called "Fact" tables
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS fact_sales (
        order_id TEXT PRIMARY KEY,
        customer_name TEXT,
        product TEXT,
        quantity INTEGER,
        price REAL,
        order_date DATE,
        country TEXT,
        total_sale REAL
    )
    '''
    cursor.execute(create_table_query)

    # 4. Load the data!
    # Pandas makes this incredibly easy. It handles all the "INSERT INTO" statements behind the scenes.
    # if_exists='replace' means it will overwrite the table if we run the script multiple times.
    df.to_sql('fact_sales', conn, if_exists='replace', index=False)
    
    print(f"Successfully loaded {len(df)} clean records into 'sales_warehouse.db'.")

    # 5. Run a quick SQL query to prove the database works
    print("\n--- Database Test Query (Total Revenue by Product) ---")
    test_query = "SELECT product, SUM(total_sale) as total_revenue FROM fact_sales GROUP BY product"
    
    # We can use pandas to read SQL queries nicely into the console
    query_results = pd.read_sql(test_query, conn)
    print(query_results)

    # Always close your database connection
    conn.close()

if __name__ == "__main__":
    load_to_database()