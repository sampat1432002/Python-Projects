from tkinter import *
from PIL import ImageTk,Image

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")


# First open image
my_pic = Image.open("Images/image2.jpg")

# Resize Image
resized = my_pic.resize((50,100),Image.ANTIALIAS)

# freshly open that image
new_pic = ImageTk.PhotoImage(my_pic)

my_lab = Label(scr,image = new_pic)
my_lab.pack(pady = 20)

scr.mainloop()
