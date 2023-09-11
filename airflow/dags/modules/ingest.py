from sqlalchemy import create_engine
import pandas as pd

server_name = "DESKTOP-C3ELCEM"
database_name = "pharmacy"

# Use Windows Authentication (trusted_connection)
connection_string = f"mssql+pyodbc://{server_name}/{database_name}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string)

try:
    connection = engine.connect()
    print("Connected to the database.")
    # Perform database operations here

    list = ['pharma','pharmamed','medication','sales']
    for item in list:
        df = pd.read_csv(item + '.csv')

        # insert data into the table
        df.to_sql(item, con=engine, if_exists='replace', index=False)

    
    # Don't forget to close the connection when you're done
    connection.close()
    print("Connection closed.")
except Exception as e:
    print("Error:", e)
