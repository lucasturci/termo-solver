import pyodbc
import json
from crawler import Crawler

# Get termo solution
crawler = Crawler()
sol = crawler.get_termo_solution()
print(f"Termo solution is: {sol}")
crawler.close()

# Read database credentials
with open('/run/secrets/database_credentials.json') as f:
    database_credentials = json.load(f)

# Define the connection string
connection_string = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database};UID={user};PWD={pwd}'.format(server_name=database_credentials["server_name"], database=database_credentials["database"], user=database_credentials["user"], pwd=database_credentials["pwd"])

# Connect to database
conn = pyodbc.connect(connection_string)

# Create a cursor from the connection
cursor = conn.cursor()

query = "INSERT INTO termo (data, palavra) VALUES (CONVERT(date, GETDATE()), ?)"

print("Inserting into table")
# Execute a query
cursor.execute(query, sol)

# Commit result
print("Commiting")
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

