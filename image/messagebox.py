from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title('Message Box')
def pop():
    response=messagebox.askyesno("This is my popup","hello everyone")
    Label(root, text=response).pack()
    if response ==1:
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No").pack()
Button(root, text="popup", command= pop).pack()
mainloop()