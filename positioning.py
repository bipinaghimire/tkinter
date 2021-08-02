from tkinter import *
root=Tk()
myLabel1= Label(root, text="Tkinter Program Beginning")
myLabel2= Label(root, text="I am Bipina")
myLabel3= Label(root, text="I am from Softwarica")
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
root.mainloop()