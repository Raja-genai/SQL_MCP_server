import sqlite3

conn = sqlite3.connect('database.py')
cursor= conn.cursor()
# Run a query
cursor.execute("SELECT sqlite_version();")
print(cursor.fetchone())

# Close the connection when finished
conn.close()