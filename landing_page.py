import tkinter as tk
import landing_page_movies
import landing_page_series
import catalogSystem_series
import catalogSystem_movies
import report_page

def view_movies_catalog():
    landing_page_movies.landing_screen_movies()

def view_series_catalog():
    landing_page_series.landing_screen_series()

def insert_series_catalog():
    catalogSystem_series.sCatalog()

def insert_movies_catalog():
    catalogSystem_movies.mCatalog()

def report_screen():
    report_page.report_screen()

def landing_page_view():
    # global windowland
    windowland = tk.Tk()
    windowland.title("Welcome!")
    windowland.geometry("500x650")

    Movie_CatBt = tk.Button(text="View Movie Catalog", height="2", width="30", command = view_movies_catalog)
    Series_CatBt = tk.Button(text="View Series Catalog", height="2", width="30", command = view_series_catalog)
    insert_MovieBt = tk.Button(text="Insert Movie data", height="2", width="30", command = insert_movies_catalog)
    insert_SeriesBt = tk.Button(text="Insert Series data", height="2", width="30", command = insert_series_catalog)
    ReportsBt = tk.Button(text="View Report", height="2", width="30", command = report_screen)

    welcomelabel = tk.Label(text="Welcome to Streamify app!", width="300", height="2", font=("Calibri", 13))
    choicelabel = tk.Label(text="Select from the following options")

    welcomelabel.pack()
    choicelabel.pack()

    Movie_CatBt.pack(pady=25)
    Series_CatBt.pack(pady=25)
    insert_MovieBt.pack(pady=25)
    insert_SeriesBt.pack(pady=25)
    ReportsBt.pack(pady=25)
    windowland.mainloop()

# landing_page_view()