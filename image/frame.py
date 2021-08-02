from tkinter import *
root=Tk()
root.title("FRAME")
frame = LabelFrame(root, text="My Frame", padx=25, pady=25)
frame.pack(padx=50,pady=50)

myButton = Button(frame, text="Click Me!", bg="black", fg="red")
myButton.grid(row=0,column=0)
mainloop()