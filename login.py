import tkinter as tk
import sqlite3
import landing_page
# from main import *
import landing_page_movies
import landing_page_series
import catalogSystem_series
import catalogSystem_movies
#import os

def landing_page_screen():
    # destroy_window()
    landing_page.landing_page_view()

def login_success():
    windowLog.destroy()
    # landing_page_screen
def verify_login():
    user_info2 = username1.get()
    password_info2 = password1.get()

    conn = sqlite3.connect("StreamingCatalogSystem.db")
    cursor = conn.cursor()
    statement = f"SELECT USER_ID from Person WHERE USER_ID ='{user_info2}' AND Password = '{password_info2}';"
    cursor.execute(statement)
    access_count = 0
    if not cursor.fetchone():  # An empty result evaluates to False.
        print("Login failed.");
        verify_login()
    else:
        # 'ON SUCCESSFUL LOGIN'
        access_count += 1
        print("Welcome!")
        stmt2 = f"SELECT USER_ID, COUNT(ACCESS_COUNT) FROM Person WHERE USER_ID ='{user_info2}' AND Access_Count = {access_count};"
        cursor.execute(stmt2)
        cursor.close()
        login_success()
        landing_page_screen()
        # landing_page.landing_page_view()
        # tk.Button(windowLog, text="OK", command=landing_page_screen).grid(row=7, pady=(20, 10), padx=(150, 10))
        #print("USER_ID: {}".format(user_info2))
        #print("Access Count: {}".format(access_count))



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

# login()