from tkinter import *
import sqlite3

root =Tk()
root.title('CT4029 - Learn how to link SQLite database with GUI in Python ! ')

#iconbitmap(bitmap) sets the icon of the window/frame widget to bitmap.
# The bitmap must be an ico type, but not png or jpg type, otherwise, the image will not display as the icon.
root.iconbitmap('gui_icon.ico')

root.geometry('400x400')


#creare a database or connect to one
conn = sqlite3.connect('SQLite_Python_Database_GUI.db')

#create cursor
cursor = conn.cursor()
#crete submit function for database
def submit():
    #create the text boxes
    id.delete(0, END)
    name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)


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


#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()


