import tkinter as tk
from tkinter import *
from main import *


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
    fName = tk.Entry(windowReg)
    lName = tk.Entry(windowReg)
    email = tk.Entry(windowReg)
    username = tk.Entry(windowReg)
    password = tk.Entry(windowReg, show="*")

    #defined the buttons to save or go back
    tk.Button(windowReg, text = "Back", command=windowReg.destroy).grid(row=5,pady=(20,10), padx=(150,10))
    tk.Button(windowReg, text = "Sign in").grid(row=6,pady=(20,10), padx=(150,10))



    #Setup the grid and added padding to the entry fields
    fName.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    lName.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    email.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    username.grid(row=3, column=1, pady=(20,10), padx=(20,20))
    password.grid(row=4, column=1, pady=(20,10), padx=(20,20))



    windowReg.mainloop()