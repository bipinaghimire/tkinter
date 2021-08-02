from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title('Inserting Image')
status = Label(root, text="image 1 to 5")
root.iconbitmap('C:/Users/user/Desktop/tkinter/image.ico')
my_image=ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/tkinter/angrybird.ico'))
my_label=Label(image= my_image)
my_label.pack()
button_quit=Button(root, text="Exit", command=root.quit, width=20)
button_quit.pack()
root.mainloop()
