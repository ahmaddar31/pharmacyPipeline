import pymysql
import pandas as pd

# Replace the placeholders with your actual database credentials
try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="pharmacy"
    )
    print("Connected to MySQL database")
    cursor = conn.cursor()
    # Extract data from tables and store in CSV files
    table_list = ['pharma', 'pharmamed', 'medication', 'sales']
    for table_name in table_list:
        # Fetch column names from the table
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [column[0] for column in cursor.fetchall()]

        # Fetch data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # Create a DataFrame with column names and data
        df = pd.DataFrame(data, columns=columns)

        # Save data to a CSV file
        df.to_csv(f"{table_name}.csv", index=False)
        print(f"{table_name} data saved to CSV file")


except pymysql.Error as err:
    print(f"Error: {err}")

