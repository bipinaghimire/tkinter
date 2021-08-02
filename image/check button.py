from tkinter import *
root = Tk()
var = StringVar()
def show():
    myLabel = Label(root, text= var.get()).pack()
checkbutton = Checkbutton(root, text="check this box", variable=var, onvalue= "Active", offvalue="Unactive")
#automatic selection will be removed.
checkbutton.deselect()
checkbutton.pack()

mybutton = Button(root, text="show selection", command= show).pack()
root.mainloop()
