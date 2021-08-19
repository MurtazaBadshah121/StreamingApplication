import tkinter as tk
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
import sqlite3 as sql

def chart():
    db = "StreamingCatalogSystem.db"
    conn = sql.connect(db)

    query = '''select Genre_Type, count(*) as Total from Movies group by Genre_Type'''
    df = pd.read_sql_query(query, conn)

    x = df['Genre_Type']
    y = df['Total']
    plt.bar(x,y)
    plt.show()
    conn.close()

def rep_tab():
#Making connection with the DB
    my_conn = sql.connect("StreamingCatalogSystem.db")

    ##### tkinter window ######
    my_rep1 = tk.Tk()
    my_rep1.geometry("1000x500")

    headTup = ('MovieID', 'Title', 'ArtistName', 'ReleaseDate', 'Duration', 'Genre', 'MovieLikes')
    r_set=my_conn.execute("""select * from Movies order by MovieLikes desc;""");
    i=1 # row value inside the loop
    headIns = 0
    for x in range(len(headTup)):
        # print(j)
        e = Entry(my_rep1, width=20, fg='red')
        e.grid(row=0, column=x)
        e.insert(END, headTup[x])

    for movie in r_set:
        # print(movie)
        for j in range(len(movie)):
            # print(j)
            e = Entry(my_rep1, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i=i+1
    # print(type(r_set))
    my_conn.close()
    my_rep1.mainloop()

def report_screen():
    my_Rep = tk.Tk()
    my_Rep.geometry("400x400")

    tk.Label(my_Rep, text="Available Reports!", width="300", height="2", font=("Calibri", 13)).pack()
    tk.Label(my_Rep, text="Select from the following options").pack()

    tk.Button(my_Rep, text="Movie list based on their popularity", height="2", width="30", command=rep_tab).pack(pady=25)
    tk.Button(my_Rep, text="Total Movies by Genere", height="2", width="30", command=chart).pack(pady=25)

    my_Rep.mainloop()
# report_screen()
# rep_tab()