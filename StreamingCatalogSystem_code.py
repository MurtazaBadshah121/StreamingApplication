import sqlite3
#import os
from sqlite3 import Error


'''the function below called create_connection() returns a Connection object 
which represents an SQLite3 database specified by the database file parameter db_file.'''

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    #change the path you want to place the database in your computer
    # db = r"C:\Users\Che\Desktop\ProjectPBD\TOGIT0817\vent\StreamingCatalogSystem.db"
    #db = r"C:\Users\murta\OneDrive\Documents\GitHub\StreamingApplication\StreamingCatalogSystem.db"
    db = r"E:\Conestoga\PythonForBigData\Project_code_git\StreamingCatalogSystem.db"

    sql_person_table = """CREATE TABLE IF NOT EXISTS Person (
                            PersonID INTEGER PRIMARY KEY,
                            FirstName TEXT NOT NULL, 
                            LastName TEXT NOT NULL,
                            EMAIL TEXT NOT NULL, 
                            USER_ID TEXT NOT NULL, 
                            Password TEXT NOT NULL,
                            Access_Count INTEGER DEFAULT 0
                        );"""

    sql_AdminLogin_table = """CREATE TABLE IF NOT EXISTS AdminLogin (
                            UserId INTEGER PRIMARY KEY,
                            USER_ID TEXT NOT NULL, 
                            Password TEXT NOT NULL, 
                            Access_Count INTEGER DEFAULT 0,
                            FOREIGN KEY (USER_ID) REFERENCES Person (USER_ID)
                        );"""

    sql_UserLogin_table = """CREATE TABLE IF NOT EXISTS UserLogin (
                            UserId INTEGER PRIMARY KEY,
                            USER_ID TEXT NOT NULL, 
                            Password TEXT NOT NULL, 
                            Access_Count INTEGER DEFAULT 0,
                            FOREIGN KEY (USER_ID) REFERENCES Person (USER_ID)
                        );"""

    sql_Artist_table = """CREATE TABLE IF NOT EXISTS Artist (
                            ArtistID INTEGER PRIMARY KEY,
                            Artist_Name TEXT
                        );"""

    sql_Genre_table = """CREATE TABLE IF NOT EXISTS Genre (
                            GenreId INTEGER PRIMARY KEY,
                            Genre_Type TEXT
                        );"""

    sql_Movies_table = """CREATE TABLE IF NOT EXISTS Movies (
                            Movie_ID INTEGER PRIMARY KEY, 
                            Title TEXT, 
                            Artist_Name TEXT,
                            ReleasedDate INTEGER,
                            Duration TEXT,
                            Genre_Type INTEGER,
                            MovieLikes INTEGER DEFAULT 0,
                            FOREIGN KEY (Artist_Name) REFERENCES Artist (Artist_Name)
                            FOREIGN KEY (Genre_Type) REFERENCES Genre (Genre_Type)
                        );"""

    sql_Series_table = """CREATE TABLE IF NOT EXISTS Series (
                            Series_ID INTEGER PRIMARY KEY, 
                            Title TEXT, 
                            Artist_Name TEXT,
                            ReleasedDate INTEGER,
                            NumSeason INTEGER,
                            NumEpisode INTEGER,
                            Genre_Type INTEGER,
                            SeriesLikes INTEGER DEFAULT 0,
                            FOREIGN KEY (Genre_Type) REFERENCES Genre (Genre_Type)
                            FOREIGN KEY (Artist_Name) REFERENCES Artist (Artist_Name)
                        );"""

    sql_Logs_table = """CREATE TABLE IF NOT EXISTS Logs (
                            LogId INTEGER PRIMARY KEY,
                            USER_ID TEXT,
                            Movie_ID INTEGER,
                            WatchedTime DateTime,
                            FOREIGN KEY (USER_ID) REFERENCES Person (USER_ID)
                            FOREIGN KEY (Movie_ID) REFERENCES Movies (Movie_ID)
                        );"""


    # create a database connection
    conn = create_connection(db)

    # create tables
    if conn is not None:
        # create person table
        create_table(conn, sql_person_table)

        # create admin table
        create_table(conn, sql_AdminLogin_table)

        # create user table
        create_table(conn, sql_UserLogin_table)

        # create artist table
        create_table(conn, sql_Artist_table)

        # create genre table
        create_table(conn, sql_Genre_table)

        # create movies table
        create_table(conn, sql_Movies_table)

        # create series table
        create_table(conn, sql_Series_table)

        # create logs table
        create_table(conn, sql_Logs_table)

    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
        main()



