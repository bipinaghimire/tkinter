from tkinter import *
root = Tk()
clicked= StringVar()
clicked.set("Monday")
def show():
    mylabel = Label(root, text=clicked.get()).pack()

#options in list
options=["Monday","Tuesday","Wednesday","Thursday","Friday"]

drop= OptionMenu(root, clicked,*options)
drop.pack()

mybutton= Button(root, text="Show selecton", command=show).pack()
exit= Button(root, text="Exit", command=root.quit).pack()
root.mainloop()