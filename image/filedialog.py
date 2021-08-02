
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')
root.iconbitmap('C:/Users/user/Desktop/tkinter/image.ico')
root.geometry('500x500')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="Documents",
                                               title="Select a file",
                                               filetypes=(("ico files", "*.ico"),
                                                          ("all files", "*.*")))


    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()
btn = Button(root, text="close", command= root.quit).pack()

mainloop()

