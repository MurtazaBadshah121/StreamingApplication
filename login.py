import tkinter as tk

def login():
    # Initial setup of the window
    windowLog = tk.Tk()
    windowLog.title("Enter your details!")

    #Defined the login labels
    tk.Label(windowLog, text="username: ").grid(row=0,pady=(20,10), padx=(10,10))
    tk.Label(windowLog, text="password: ").grid(row=1,pady=(20,10), padx=(10,10))

    #Defined the buttons to save or go back
    tk.Button(windowLog, text = "Back", command=windowLog.destroy).grid(row=5,pady=(20,10), padx=(150,10))
    tk.Button(windowLog, text = "Sign in").grid(row=6,pady=(20,10), padx=(150,10))

    #Defined the text entry fields
    username = tk.Entry(windowLog)
    password = tk.Entry(windowLog, show="*")

    #Adjusting the layout and grid
    username.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    password.grid(row=1, column=1, pady=(20,10), padx=(20,20))


    #Run the window
    windowLog.mainloop()