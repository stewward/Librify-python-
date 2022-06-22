#Second Iteration 
import sqlite3

#1. Connect the database 
conn = sqlite3.connect("lite.db")
#2. Create a cursor object  
cur = conn.cursor()
#3. Apply a SQL query 
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
#4. Commit your changes to the database 
conn.commit()
#5. Close the connection 
conn.close()