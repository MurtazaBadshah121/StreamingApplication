import tkinter as tk
from tkcalendar import Calendar,DateEntry
import sqlite3


def exitserieCat():
    windowCat.destroy()

def SerieEntry():
    sTitle_entry = sTitle.get()
    sDate_entry = sDate.get()
    nSeasons_entry = nSeasons.get()
    nEpisodes_entry = nEpisodes.get()
    nGenre_entry = nGenre.get()
    nArtistName_entry = nArtistName.get()
    nLikes_entry = nLikes.get()

    try:
        conn = sqlite3.connect("StreamingCatalogSystem.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Genre (Genre_Type) VALUES ('{}');""".format
                       (nGenre_entry))

        cursor.execute("""INSERT INTO Artist (Artist_Name) VALUES ('{}');""".format
                       (nArtistName_entry))

        cursor.execute("""INSERT INTO Series (Title, Artist_Name, ReleasedDate, NumSeason, NumEpisode, Genre_Type, SeriesLikes ) VALUES (?,?,?,?,?,?,?)""",
                   (sTitle_entry, nArtistName_entry, sDate_entry, nSeasons_entry, nEpisodes_entry, nGenre_entry, nLikes_entry))


        # commit the changes to db
        conn.commit()

        tk.Label(windowCat, text="Serie entry has been recorded.").grid(row=10)
        tk.Button(windowCat, text="OK", command=exitserieCat).grid(row=9, pady=(20, 10), padx=(150, 10))
        cursor.close()

    except ValueError:
        print("Invalid input.")


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
    tk.Label(windowCat, text="Genre: ").grid(row=4, pady=(20, 10), padx=(10, 10))
    tk.Label(windowCat, text="Artist: ").grid(row=5, pady=(20, 10), padx=(10, 10))
    tk.Label(windowCat, text="No. of Likes: ").grid(row=6,pady=(20,10), padx=(10,10))

    #Defined the entry fields.
    global sTitle
    global sDate
    global nSeasons
    global nEpisodes
    global nGenre
    global nArtistName
    global nLikes

    sTitle = tk.Entry(windowCat)
    sDate = DateEntry(windowCat,width=30,bg="darkblue",fg="white",year=2010)
    nSeasons = tk.Entry(windowCat)
    nEpisodes = tk.Entry(windowCat)
    nGenre = tk.Entry(windowCat)
    nArtistName = tk.Entry(windowCat)
    nLikes = tk.Entry(windowCat)

    #defined the buttons to save or go back
    tk.Button(windowCat, text = "Back",height="2", width="30", command=windowCat.destroy).grid(row=7,pady=(20,10), padx=(150,10))
    tk.Button(windowCat, text = "Save",height="2", width="30", command=SerieEntry).grid(row=8,pady=(20,10), padx=(150,10))

    #Setup the grid and added padding to the entry fields
    sTitle.grid(row=0, column=1, pady=(20,10), padx=(20,20))
    sDate.grid(row=1, column=1, pady=(20,10), padx=(20,20))
    nSeasons.grid(row=2, column=1, pady=(20,10), padx=(20,20))
    nEpisodes.grid(row=3, column=1, pady=(20,10), padx=(20,20))
    nLikes.grid(row=6, column=1, pady=(20,10), padx=(20,20))
    nGenre.grid(row=4, column=1, pady=(20, 10), padx=(20, 20))
    nArtistName.grid(row=5, column=1, pady=(20, 10), padx=(20, 20))


    windowCat.mainloop()

# sCatalog()