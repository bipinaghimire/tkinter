from tkinter import *
root=Tk()
a= Entry(root, width=50, fg = "blue",bg="white", borderwidth=5)
a.pack()
def myClick():
    textoutput="Hello " + a.get()
    myLabel= Label(root, text= textoutput)
    myLabel.pack()
myButton= Button(root, text="click Me!", command= myClick, bg="black", fg="green")
myButton.pack()
root.mainloop()