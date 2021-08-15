import tkinter as tk
from tkinter import *
from login import *
from registration import *


def onclick():
    login()

def onclick2():
    register()

def main_screen():
    window = tk.Tk()
    window.title("Welcome!")
    window.geometry("300x250")


    #Create a form label
    welcomelabel = tk.Label(text="Welcome to Streamify app!", width="300", height="2", font=("Calibri", 13))
    choicelabel = tk.Label(text="Please log in or create a new account")


    btLogin = tk.Button(text="Log in", height="2", width="30", command = onclick)
    btRegister = tk.Button(text="Register", height="2", width="30", command = onclick2)


#welcomelabel.grid(row=0, column=0)
#choicelabel.grid(row=1, column=0)
#btLogin.grid(row=2, column=0)
#btRegister.grid(row=3, column=0)

    welcomelabel.pack()
    choicelabel.pack()
    btLogin.pack(pady=25)
    btRegister.pack()
    #frame_a.pack()
    #frame_b.pack()

    window.mainloop()

if __name__ == '__main__':
    main_screen()