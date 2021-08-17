import tkinter as tk
from tkcalendar import Calendar,DateEntry


def sCatalog():
    # Initial setup of the window
    global windowCat
    windowCat = tk.Tk()
    windowCat.title("Enter Series information")

    #Defined the labels for the text entry fields below.
    tk.Label(windowCat, text="Title: ").grid(row=0, pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="Release date: ").grid(row=1,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="No. of Seasons: ").grid(row=2,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="No. of Episodes: ").grid(row=3,pady=(20,10), padx=(10,10))
    tk.Label(windowCat, text="No. of Likes: ").grid(row=4,pady=(20,10), padx=(10,10))

    #Defined the entry fields.
    global sTitle
    global sDate
    global nSeasons
    global nEpisodes
    global nLikes

    sTitle = tk.Entry(windowCat)
    sDate = DateEntry(windowCat,width=30,bg="darkblue",fg="white",year=2010)
    nSeasons = tk.Entry(windowCat)
    nEpisodes = tk.Entry(windowCat)
    nLikes = tk.Entry(windowCat)

    #defined the buttons to save or go back
    tk.Button(windowCat, text = "Back",height="2", width="30", command=windowCat.destroy).grid(row=5,pady=(20,10), padx=(150,10))
    tk.Button(windowCat, text = "Save",height="2", width="30").grid(row=6,pady=(20,10), padx=(150,10))

    #Setup the grid and added padding to the entry fields
    sTitle.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    sDate.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    nSeasons.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    nEpisodes.grid(row=3, column=1, pady=(20,10), padx=(20,20))
    nLikes.grid(row=4, column=1, pady=(20,10), padx=(20,20))

    windowCat.mainloop()

sCatalog()