import tkinter as tk
from tkinter import *
import sqlite3

def exitwindow():
    windowReg.destroy()

def reg_user():
    fname_info = fName.get()
    lname_info = lName.get()
    email_info = email.get()
    user_info = username.get()
    password_info = password.get()

    try:
        conn = sqlite3.connect("StreamingCatalogSystem.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Person (FirstName, Lastname, EMAIL, USER_ID, Password) VALUES (?,?,?,?,?)""",
                   (fname_info, lname_info, email_info, user_info, password_info))

        cursor.execute("""INSERT INTO UserLogin (USER_ID, Password) VALUES (?,?)""",
                       (user_info, password_info))

        cursor.execute("""INSERT INTO AdminLogin (USER_ID, Password) VALUES (?,?)""",
                       (user_info, password_info))

        # commit the changes to db
        conn.commit()

        username.delete(0, END)
        password.delete(0, END)
        fName.delete(0, END)
        lName.delete(0, END)
        email.delete(0, END)

        Label(windowReg, text="Registered successfully.")

        tk.Button(windowReg, text = "Exit", command=exitwindow).grid(row=7,pady=(20,10), padx=(150,10))
    except ValueError:
        print("Invalid input.")

def register():
    # Initial setup of the window
    global windowReg
    windowReg = tk.Tk()
    windowReg.title("Enter your details")

    #Defined the labels for the text entry fields below.
    tk.Label(windowReg, text="First Name: ").grid(row=0, pady=(20,10), padx=(10,10))
    tk.Label(windowReg, text="Last Name: ").grid(row=1,pady=(20,10), padx=(10,10))
    tk.Label(windowReg, text="Email: ").grid(row=2,pady=(20,10), padx=(10,10))
    tk.Label(windowReg, text="username: ").grid(row=3,pady=(20,10), padx=(10,10))
    tk.Label(windowReg, text="password: ").grid(row=4,pady=(20,10), padx=(10,10))

    #Defined the entry fields.
    global fName
    global lName
    global email
    global username
    global password
    fName = tk.Entry(windowReg)
    lName = tk.Entry(windowReg)
    email = tk.Entry(windowReg)
    username = tk.Entry(windowReg)
    password = tk.Entry(windowReg, show="*")

    #defined the buttons to save or go back
    tk.Button(windowReg, text = "Back", command=windowReg.destroy).grid(row=5,pady=(20,10), padx=(150,10))
    tk.Button(windowReg, text = "Sign in", command=reg_user).grid(row=6,pady=(20,10), padx=(150,10))

    #Setup the grid and added padding to the entry fields
    fName.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    lName.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    email.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    username.grid(row=3, column=1, pady=(20,10), padx=(20,20))
    password.grid(row=4, column=1, pady=(20,10), padx=(20,20))

    windowReg.mainloop()


#register()
