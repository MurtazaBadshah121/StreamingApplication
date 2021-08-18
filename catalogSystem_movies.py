import tkinter as tk
from tkinter import *
from tkcalendar import Calendar,DateEntry
import sqlite3


def exitmovieCat():
    windowCat.destroy()

def movieEntry():
    mtitle_entry = mTitle.get()
    mdate_entry = rDate.get()
    mduration = duration.get()
    genre_entry = genre.get()
    artistname_entry = artistname.get()
    #mLikes.get()

    try:
        conn = sqlite3.connect("StreamingCatalogSystem.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Genre (Genre_Type) VALUES ('{}');""".format
                       (genre_entry))

        cursor.execute("""INSERT INTO Artist (Artist_Name) VALUES ('{}');""".format
                       (artistname_entry))

        cursor.execute("""INSERT INTO Movies (Title, Artist_Name, ReleasedDate, Duration, Genre_Type) VALUES (?,?,?,?,?)""",
                   (mtitle_entry, artistname_entry, mdate_entry, mduration, genre_entry))


        # commit the changes to db
        conn.commit()

        # mTitle.delete(0, END)
        # #mdate_entry.delete(0, END)
        # # mduration.delete(0, END)
        # genre_entry.delete(0, END)
        # artistname_entry.delete(0, END)
        # medianame_entry.delete(0, END)

        tk.Label(windowCat, text="Movie entry has been recorded.").grid(row=8)
        tk.Button(windowCat, text="OK", command=exitmovieCat).grid(row=9, pady=(20, 10), padx=(150, 10))

    except ValueError:
        print("Invalid input.")

def mCatalog():
    # Initial setup of the window
    global windowCat
    windowCat = tk.Tk()
    windowCat.title("Enter Movie information")

    #Defined the labels for the text entry fields below.
    tk.Label(windowCat, text="Title: ").grid(row=0, pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Release date: ").grid(row=1,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Duration: ").grid(row=2,pady=(20,10), padx=(10,10))
    #tk.Label(windowCat, text="MovieLikes: ").grid(row=3,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Genre: ").grid(row=3, pady=(20, 10), padx=(10, 10))
    tk.Label(windowCat, text="Artist Name: ").grid(row=4, pady=(20, 10), padx=(10, 10))

    #Defined the entry fields.
    global mTitle
    global rDate
    global duration
    global genre
    global artistname
    #global mLikes

    mTitle = tk.Entry(windowCat)
    rDate = DateEntry(windowCat,width=30,bg="darkblue",fg="white",year=2010)
    duration = tk.Entry(windowCat)
    genre = tk.Entry(windowCat)
    artistname = tk.Entry(windowCat)
    #mLikes = tk.Entry(windowCat)

    #defined the buttons to save or go back
    tk.Button(windowCat, text = "Back",height="2", width="30", command=exitmovieCat).grid(row=5,pady=(20,10), padx=(200,10))
    tk.Button(windowCat, text = "Save",height="2", width="30", command=movieEntry).grid(row=6,pady=(20,10), padx=(200,10))

    #Setup the grid and added padding to the entry fields
    mTitle.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    rDate.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    duration.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    genre.grid(row=3, column=1, pady=(20, 10), padx=(20, 20))
    artistname.grid(row=4, column=1, pady=(20, 10), padx=(20, 20))
    #mLikes.grid(row=3, column=1, pady=(20,10), padx=(20,20))

    windowCat.mainloop()

# mCatalog()