import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")


    sql_update_query = 'UPDATE Employee SET name="Mark" WHERE email="csev@glos.ac.uk"'
    cursor.execute(sql_update_query)

    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (sqliteConnection):
        print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
        sqliteConnection.close()
        print("sqlite connection is closed")











