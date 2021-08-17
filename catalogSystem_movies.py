import tkinter as tk
from tkcalendar import Calendar,DateEntry


def mCatalog():
    # Initial setup of the window
    global windowCat
    windowCat = tk.Tk()
    windowCat.title("Enter Movie information")

    #Defined the labels for the text entry fields below.
    tk.Label(windowCat, text="Title: ").grid(row=0, pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Release date: ").grid(row=1,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Duration: ").grid(row=2,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="MovieLikes: ").grid(row=3,pady=(20,10), padx=(10,10))

    #Defined the entry fields.
    global mTitle
    global rDate
    global duration
    global mLikes

    mTitle = tk.Entry(windowCat)
    rDate = DateEntry(windowCat,width=30,bg="darkblue",fg="white",year=2010)
    duration = tk.Entry(windowCat)
    mLikes = tk.Entry(windowCat)

    #defined the buttons to save or go back
    tk.Button(windowCat, text = "Back",height="2", width="30", command=windowCat.destroy).grid(row=5,pady=(20,10), padx=(200,10))
    tk.Button(windowCat, text = "Save",height="2", width="30").grid(row=6,pady=(20,10), padx=(200,10))

    #Setup the grid and added padding to the entry fields
    mTitle.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    rDate.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    duration.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    mLikes.grid(row=3, column=1, pady=(20,10), padx=(20,20))

    windowCat.mainloop()

#mCatalog()