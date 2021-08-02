from tkinter import *
root= Tk()
def myClick():
    label = Label(root,text="Button is clicked")
    label.pack()
myButton= Button(root, text="CLICK", command=myClick, fg="red", bg="black")
myButton.pack()
root.mainloop()