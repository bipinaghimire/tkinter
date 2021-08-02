from tkinter import *
root = Tk()
root.title('Slider')

vertical = Scale(root, from_=0, to=500)
vertical.pack()

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)
horizontal.pack()
def slide():
    my_label = Label(root, text=horizontal.get()).pack()

    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_btn = Button(root, text="Click Me", command=slide).pack()

mainloop()