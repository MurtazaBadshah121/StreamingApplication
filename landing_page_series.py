import tkinter as tk
from tkinter import *
import sqlite3

def landing_screen_series():
    #Making connection with the DB
    my_conn = sqlite3.connect("StreamingCatalogSystem.db")

    ##### tkinter window ######
    my_w = tk.Tk()
    my_w.geometry("1000x450")

    headTup = ('SeriesID', 'Title', 'ArtistName', 'ReleaseDate', 'NumSeason', 'NumEpisodes', 'GenreType', 'SeriesLikes')
    r_set=my_conn.execute('''SELECT * from Series''');
    i=1 # row value inside the loop
    headIns = 0
    for x in range(len(headTup)):
        # print(j)
        e = Entry(my_w, width=20, fg='red')
        e.grid(row=0, column=x)
        e.insert(END, headTup[x])

    for series in r_set:
        # print(series)
        for j in range(len(series)):
            # print(j)
            e = Entry(my_w, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, series[j])
        i=i+1
    print(type(r_set))
    my_w.mainloop()

# landing_screen_series()