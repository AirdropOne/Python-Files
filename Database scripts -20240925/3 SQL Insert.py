import sqlite3
import traceback
import sys

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = 'INSERT INTO Users (name, email) VALUES ("John", "JH@glos.ac.uk")' #SQL insert
    sqlite_insert2_query='INSERT INTO Employee (id,name,email) VALUES (110,"Charles", "amd@glos.ac.uk")' #SQL insert

    count = cursor.execute(sqlite_insert_query)#first SQL insert query execution
    count=cursor.execute(sqlite_insert2_query)#second SQL insert query execution
    sqliteConnection.commit()
    print("Record inserted successfully into Users table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")