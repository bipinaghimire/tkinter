from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title('image viewer')
root.iconbitmap('C:/Users/user/Desktop/tkinter/image.ico')
myimage1= ImageTk.PhotoImage(Image.open("C:/Users/user/Desktop/tkinter/doctor.ico"))
myimage2= ImageTk.PhotoImage(Image.open("C:/Users/user/Desktop/tkinter/angrybird.ico"))
myimage3= ImageTk.PhotoImage(Image.open("C:/Users/user/Desktop/tkinter/simpsons.ico"))
myimage4= ImageTk.PhotoImage(Image.open("C:/Users/user/Desktop/tkinter/lion.ico"))
list=[myimage1, myimage2, myimage3, myimage4]
mylabel= Label(image=myimage1)
mylabel.grid(row=0, column=0, columnspan=3)

status = Label(root, text="1 of " + str(len(list)), bd=2, relief=SUNKEN, anchor=E)

def forward(numbers):
    global mylabel
    global forbutton
    global backbutton
    mylabel.grid_forget()
    mylabel = Label(image=list[numbers-1])
    forbutton = Button(root, text="next", command=lambda: forward(numbers+1))
    backbutton = Button(root, text="back", command=lambda: backward(numbers - 1))
    if numbers==4:
        forbutton= Button(root, text="next", state= DISABLED)
    mylabel.grid(row=0, column=0, columnspan=3)
    backbutton.grid(row=1, column=0)
    forbutton.grid(row=1, column=2)

    status = Label(root, text=str(numbers) + " of " + str(len(list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(numbers):
    global mylabel
    global forbutton
    global backbutton
    mylabel.grid_forget()
    mylabel = Label(image=list[numbers - 1])
    forbutton = Button(root, text="next", command=lambda: forward(numbers + 1))
    backbutton = Button(root, text="back", command=lambda: backward(numbers - 1))

    if numbers == 1:
        backbutton = Button(root, text="back", state=DISABLED)
    mylabel.grid(row=0, column=0, columnspan=3)
    backbutton.grid(row=1, column=0)
    forbutton.grid(row=1, column=2)

    status = Label(root, text=str(numbers) + " of " + str(len(list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


buttonexit= Button(root, text="exit", command= root.quit, width=25)
backbutton= Button(root, text="back", command= backward, state= DISABLED)
forbutton= Button(root, text="next", command=lambda:forward(2))

buttonexit.grid(row=1, column=1)
backbutton.grid(row=1, column=0)
forbutton.grid(row=1, column=2)

status.grid(row=2,column=0,columnspan=3, sticky=W+E)

root.mainloop()
