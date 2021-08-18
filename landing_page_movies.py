import tkinter as tk
from tkinter import *
import sqlite3

def landing_screen_movies():
    #Making connection with the DB
    my_conn = sqlite3.connect("StreamingCatalogSystem.db")

    ##### tkinter window ######
    my_w = tk.Tk()
    my_w.geometry("870x450")

    headTup = ('MovieID', 'Title', 'ArtistName', 'ReleaseDate', 'Duration', 'Genre', 'MovieLikes')
    r_set=my_conn.execute('''SELECT * from Movies''');
    i=1 # row value inside the loop
    headIns = 0
    for x in range(len(headTup)):
        # print(j)
        e = Entry(my_w, width=20, fg='red')
        e.grid(row=0, column=x)
        e.insert(END, headTup[x])

    for movie in r_set:
        # print(movie)
        for j in range(len(movie)):
            # print(j)
            e = Entry(my_w, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i=i+1
    print(type(r_set))
    my_w.mainloop()

# landing_screen_movies()