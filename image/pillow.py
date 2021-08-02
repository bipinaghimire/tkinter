from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title('Inserting Image')
root.iconbitmap('C:/Users/user/Desktop/Hospital_icon-icons.com_74918.ico')
my_image=ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/Hospital_icon-icons.com_74918.ico'))
my_label=Label(image= my_image)
my_label.pack()
button_quit=Button(root, text="Exit", command=root.quit, width=20)
button_quit.pack()
root.mainloop()
