## Get user to input email and password
## Check that the email and password correlate with the same ID in database
## If yes :Enter, If no :Invalid
## UI text for login, email and password
## Text input field for email and password
## Login button that links to the credential check function

import mysql.connector
import tkinter
import sqlite3
from tkinter import messagebox



def login():
    email = email_entry.get()                                                           ## assigning a name to the function of pulling the values that have been input into the email entry field
    password = password_entry.get()                                                     ## ''
    
    connect = sqlite3.connect("practise_DB.db")                                         ## assigning a name to the funtion of connecting to my practise datatbase         and       remember the .db
    c = connect.cursor()                                                                ## assigning a name to the function of making a request to the connected database

    c.execute("SELECT * FROM Login_Database WHERE Email=? AND Password=?", (email, password))  ## "?" work as a placeholder for the tuple values
    
    row=c.fetchone()                                                                    ## goes one by one along a row
    if row:
        messagebox.showinfo("info", "login success")
    else:
        messagebox.showinfo("info", "login failed")



def register():
    email = email_reg.get()
    password = password_reg.get() 

    connect = sqlite3.connect("practise_DB.db")
    c = connect.cursor()

    c.execute("INSERT INTO Login_Database (Email, Password", (email, password))



def open_registration_window():
    reg_window=tkinter.Tk()
    reg_window.title("Registration Page")
    reg_window.geometry("400x300")
    padd=20
    reg_window["padx"]=padd
    info_label=tkinter.Label(reg_window, text ="Registration Page")
    info_label.grid(row=0, column=0)

    email_label=tkinter.Label(reg_window, text ="Email")
    email_label.grid(row=1, column=0)

    email_reg=tkinter.StringVar

    email_reg=tkinter.Entry(reg_window, textvariable=email_reg)
    email_reg.grid(row=1, column=1)

    password_label=tkinter.Label(reg_window, text="Password")
    password_label.grid(row=2, column=0)

    password_reg=tkinter.StringVar

    password_reg=tkinter.Entry(reg_window, textvariable=password_reg)
    password_reg.grid(row=2, column=1)


    register_button=tkinter.Button(reg_window, text="Register", command=register)
    register_button.grid(row=4, column=1, pady=5)






main_window=tkinter.Tk()                                                                ## Creating the main page
main_window.title("Login_page")                                                         ## What its called
main_window.geometry("400x300")                                                         ## Its size
padd=20                                                             
main_window["padx"]=padd
info_label=tkinter.Label(main_window, text ="Login Page")                               ## Labeling the top left
info_label.grid(row=0, column=0)                                                        ## Defining the location on a grid




info_email=tkinter.Label(main_window, text ="Email")                                    ## Labeling the Email text
info_email.grid(row=1, column=0)                                                        ## Placing that text within the grid

email_entry=tkinter.StringVar()                                                         ## Storing the entry as a string - WHY???? - SQL sanitisation???

email_entry=tkinter.Entry(main_window, textvariable=email_entry)                        ## Assigning a name to en entry field           and            Specifying we want to use tkinters .StringVar as the text type for this field
email_entry.grid(row=1, column=1)                                                       ## Placing that entry field in the grid



info_password=tkinter.Label(main_window, text = "Password")                             ## Repeating for password - Remember we dont want to repeat code? Generalise thi code so instead of password or email, just "input" ?
info_password.grid(row=2, column=0)                                                     ## ''

password_entry=tkinter.StringVar()                                                      ## ''

password_entry=tkinter.Entry(main_window, textvariable=password_entry, show="*")        ## ''    and show="*" shows inputs as * for (for password protection)
password_entry.grid(row=2, column=1)                                                    ## ''


                            

login_button=tkinter.Button(main_window, text="Login", command=login)                   ## Assigning a name and adding text login button        and       initiate the login function
login_button.grid(row=3, column=1, pady=5)                                              ## Placing the button in the grid

create_account_button=tkinter.Button(main_window, text="Create Account", command=open_registration_window)                ## Assigning a name and adding text to create accountbutton       and      initiate page traversal??
create_account_button.grid(row=4, column=1, pady=5)                                     ## Placing the button in the grid



main_window.mainloop()                                                                  ## Infinite loop for main page

