import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('database.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()
    query = "CREATE TABLE tickets(id integer PRIMARY KEY, username varchar(50), phonenumber integer, timings varchar(6))";
    try:
    	cursorObj.execute(query)
    	print("Table created successfully!")
    except:
    	print("Table creation failed.");
    con.commit()

con = sql_connection()

sql_table(con)