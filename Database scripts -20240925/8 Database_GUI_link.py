from tkinter import *
import sqlite3

root =Tk()
root.title('CT4029 - Learn how to link SQLite database with GUI in Python ! ')

#iconbitmap(bitmap) sets the icon of the window/frame widget to bitmap.
# The bitmap must be an ico type, but not png or jpg type, otherwise, the image will not display as the icon.
root.iconbitmap('gui_icon.ico')

root.geometry('400x400')



#crete submit function for database
def submit():
    conn = sqlite3.connect('SQLite_Python_Database_GUI.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Employee VALUES (:id, :name, :email, :password)",
                   #create dictionory (we will cover that next week :)
                   {
                       'id': id.get(),
                       'name': name.get(),
                       'email': email.get(),
                       'password': password.get()
                   })
    conn.commit()
    conn.close()
    #create the text boxes
    id.delete(0, END)
    name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)

#create query function
def query():
    conn = sqlite3.connect('SQLite_Python_Database_GUI.db')
    cursor = conn.cursor()

    #query the database
    cursor.execute("SELECT * FROM Employee")
    records=cursor.fetchall()
    #return a python list, and tuples in the list
    #print(records)
    print_record=''
    for record in records:
        print_record += str(record[1]) + "   " + str(record[2]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)
    conn.commit()
    conn.close()

#create text boxes
id = Entry(root, width=30)
id.grid(row=0, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=1, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=2, column=1, padx=20)
password = Entry(root, width=30)
password.grid(row=3, column=1, padx=20)


#create text box labels
id_label = Label(root, text='Employer ID')
id_label.grid(row=0, column=0)
name_label = Label(root, text='Last Name')
name_label.grid(row=1, column=0)
email_label = Label(root, text='Email')
email_label.grid(row=2, column=0)
password_label = Label(root, text='Password')
password_label.grid(row=3, column=0)

#Create submit buttons
submit_btn = Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



root.mainloop()


