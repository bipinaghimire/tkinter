from tkinter import *
import sqlite3
root=Tk()
root.title('Database')
#creating database
conn= sqlite3.connect('address_book.db')

c= conn.cursor()


c.execute("""CREATE TABLE address(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
)""")

print("Table created successfully")


conn.commit()

conn.close()


mainloop()


