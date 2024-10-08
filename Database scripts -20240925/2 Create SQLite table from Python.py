import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db') #establish connection with the database
    sqlite_create_table_query = '''CREATE TABLE Users(name VARCHAR(128), 
                                    email VARCHAR(128));''' #create first table
    sqlite_create__table_query='''CREATE TABLE Employee(id INTEGER, name VARCHAR(128), email VARCHAR(128)); '''#create second table

    cursor = sqliteConnection.cursor() #Get a cursor to the database
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query) #execute the first query
    cursor.execute(sqlite_create__table_query) #execute the second query
    sqliteConnection.commit()
    print("SQLite tables created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")