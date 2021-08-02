from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root,text="Hi Bipina Ghimire", bg="black", fg="red")
    myLabel.pack()
myButton = Button(root, text="Click Me!", command=myClick, bg="black", fg="red")
myButton.pack()
root.mainloop()