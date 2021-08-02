from tkinter import *
root = Tk()
root.title("Welcome Bipina Ghimire.")
root.geometry("400x240")
sample_text = Text(root, height=10)
sample_text.pack()
Font_tuple = ("Aerial", 20, "bold")
sample_text.configure(font=Font_tuple)
root.mainloop()