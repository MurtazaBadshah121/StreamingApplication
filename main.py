import tkinter as tk
from tkinter import *
#from login import *
#from registration import *
import landing_page_movies
import landing_page_series
import catalogSystem_series
import catalogSystem_movies
import sqlite3
import landing_page

# import login
import registration

def destroy_window():
    window.destroy()

def onclick():
    login()

def onclick2():
    registration.register()

def main_screen():
    global window
    window = tk.Tk()
    window.title("Welcome!")
    window.geometry("300x250")


    #Create a form label
    welcomelabel = tk.Label(text="Welcome to Streamify app!", width="300", height="2", font=("Calibri", 13))
    choicelabel = tk.Label(text="Please log in or create a new account")


    # btLogin = tk.Button(text="Log in", height="2", width="30", command =lambda:[onclick,destroy_window])
    btLogin = tk.Button(text="Log in", height="2", width="30", command=onclick)
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




def landing_page_screen():
    # destroy_window()
    landing_page.landing_page_view()

# def login_success():
#     windowLog.destroy()
    # landing_page_screen
def verify_login():
    user_info2 = username1.get()
    password_info2 = password1.get()

    conn = sqlite3.connect("StreamingCatalogSystem.db")
    cursor = conn.cursor()
    statement = f"SELECT USER_ID from Person WHERE USER_ID ='{user_info2}' AND Password = '{password_info2}';"
    cursor.execute(statement)
    access_count = 0
    # username1.delete(0, END)
    # password1.delete(0, END)
    if not cursor.fetchone():  # An empty result evaluates to False.
        print("Login failed.");
        verify_login()
    else:
        # 'ON SUCCESSFUL LOGIN'
        access_count += 1
        print("Welcome!")
        stmt2 = f"SELECT USER_ID, COUNT(ACCESS_COUNT) FROM Person WHERE USER_ID ='{user_info2}' AND Access_Count = {access_count};"
        cursor.execute(stmt2)
        windowLog.destroy()
        destroy_window()
        landing_page_screen()
        # landing_page.landing_page_view()
        # tk.Button(windowLog, text="OK", command=landing_page_screen).grid(row=7, pady=(20, 10), padx=(150, 10))
        #print("USER_ID: {}".format(user_info2))
        #print("Access Count: {}".format(access_count))

    cursor.close()


def login():
    # Initial setup of the window
    global windowLog
    windowLog = tk.Tk()
    windowLog.title("Enter your details!")

    #Defined the login labels
    tk.Label(windowLog, text="username: ").grid(row=0,pady=(20,10), padx=(10,10))
    tk.Label(windowLog, text="password: ").grid(row=1,pady=(20,10), padx=(10,10))

    #Defined the buttons to save or go back
    tk.Button(windowLog, text = "Back", command=windowLog.destroy).grid(row=5,pady=(20,10), padx=(150,10))
    tk.Button(windowLog, text = "Sign in", command=verify_login).grid(row=6,pady=(20,10), padx=(150,10))

    #Defined the text entry fields
    global username1
    global password1
    username1 = tk.Entry(windowLog)
    password1 = tk.Entry(windowLog, show="*")

    #Adjusting the layout and grid
    username1.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    password1.grid(row=1, column=1, pady=(20,10), padx=(20,20))


    #Run the window
    windowLog.mainloop()




if __name__ == '__main__':
    main_screen()