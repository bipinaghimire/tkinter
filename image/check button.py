from tkinter import *
root = Tk()
var = StringVar()
def show():
    myLabel = Label(root, text= var.get()).pack()
checkbutton = Checkbutton(root, text="check this box", variable=var, onvalue= "On", offvalue="Off")
checkbutton.deselect()
checkbutton.pack()

mybutton = Button(root, text="show selection", command= show).pack()
root.mainloop()
