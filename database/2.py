from tkinter import *
import sqlite3
root=Tk()
root.title('Database')
#creating database
conn= sqlite3.connect('address_book.db')

c= conn.cursor()

#c.execute("""CREATE TABLE address(
#       first_name text,
#       last_name text,
#       address text,
#       city text,
#       state text,
#       zipcode integer
#)""")

#creating text boxes

f_name= Entry(root, width=30, bd=2, relief= SUNKEN)
f_name.grid(row=0, column=1, padx=20)

l_name= Entry(root, width=30, bd=2, relief= SUNKEN)
l_name.grid(row=1, column=1, padx=20)

address= Entry(root, width=30, bd=2, relief= SUNKEN)
address.grid(row=2, column=1, padx=20)

city= Entry(root, width=30, bd=2, relief= SUNKEN)
city.grid(row=3, column=1, padx=20)

state= Entry(root, width=30, bd=2, relief= SUNKEN)
state.grid(row=4, column=1, padx=20)

zipcode= Entry(root, width=30, bd=2, relief= SUNKEN)
zipcode.grid(row=5, column=1, padx=20)


#creating text box labels

f_name_label= Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label= Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label= Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label= Label(root, text="City")
city_label.grid(row=3, column=0)

state_label= Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label= Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

#creating submit button
def submit():
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

submit_button= Button(root, text="Add record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

close_button= Button(root, text="Close", command= root.quit)
close_button.grid(row=7, column=0, columnspan=2, padx=10, ipadx=100)


conn.commit()

conn.close()


mainloop()