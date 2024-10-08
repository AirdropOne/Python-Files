import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = "SELECT * FROM Employee WHERE email='csev@glos.ac.uk'" #SQL select all
    sqlite_select_query="SELECT * FROM Employee ORDER BY id"#SQL select all using order by statment as a condition
    cursor.execute(sqlite_select_query)#execute the SQL select query
    totalRows = cursor.fetchall() #cursor.fetchone()
    print("Total rows are:  ", totalRows)
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (sqliteConnection):
        print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
        sqliteConnection.close()
        print("sqlite connection is closed")












