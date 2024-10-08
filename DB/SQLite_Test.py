import sqlite3
from sqlite3 import Error as SQLError

try:
    sqliteconnection = sqlite3.connect('../SQLite_Python.db')
    
    cursor = sqliteconnection.cursor() # use cursor to perform transactions with the databse
    
    print ("Connected to Database")
    
    sql_query = """SELECT name FROM sqlite_master WHERE type = 'table'"""
    sqlite_select_query = "SELECT * FROM Users" #PUT YOUR SQL QUERY CODE IN THIS FIELD
    cursor.execute(sqlite_select_query)    ## figure out how to process a query!!
    record = cursor.fetchall()
    print(record)
    cursor.close()
    sqliteconnection.close()

    
except SQLError as error:
    print("Error connection to sqlite", error)
    
    
# import sqlite3

# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")

#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("The SQLite connection is closed")