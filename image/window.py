from tkinter import *
from PIL import ImageTk, Image
top = Tk()
def open():
    global my_img
    top=Toplevel()
    top.title('Check new window')
    top.iconbitmap('C:/Users/user/Desktop/tkinter/image.ico')
    my_img= ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/tkinter/lion.ico'))
    my_label= Label(top, image=my_img).pack()

    button= Button(top, text="Close", command= top.quit).pack()

    def open2():
        global my_img
        top=Toplevel()
        top.title('Check new window')
        top.iconbitmap('C:/Users/user/Desktop/tkinter/image.ico')
        my_img= ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/tkinter/simpsons.ico'))
        my_label= Label(top, image=my_img).pack()

        button= Button(top, text="Close", command= top.quit).pack()

btn= Button(top, text="open", command= open).pack()
btnclose = Button(top, text="close", command= top.quit).pack()

top.mainloop()

