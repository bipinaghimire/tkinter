from tkinter import *
root = Tk()
clicked= StringVar()
clicked.set("Monday")
def show():
    mylabel = Label(root, text=clicked.get()).pack()


drop= OptionMenu(root, clicked,"Monday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

mybutton= Button(root, text="Show selecton", command=show).pack()
exit= Button(root, text="Exit", command=root.quit).pack()
root.mainloop()