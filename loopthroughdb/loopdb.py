import sqlite3

conn = sqlite3.connect('mysqlite.db')
cursor = conn.cursor()

# Step 1: Get a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Step 2: Loop through all tables to check for the column
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    for column in columns:
        column_name = column[1]
        if column_name == 'eid':
            print(f"The column 'eid' exists in table {table_name}")

conn.close()
