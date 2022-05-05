from tkinter import *
from PIL import ImageTk,Image

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def change(event):
	my_pic = ImageTk.PhotoImage(Image.open("Images/image2.jpg"))
	my_lab.config(image=my_pic)
	my_lab.image = my_pic

def change_back(event):
	my_pic = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
	my_lab.config(image=my_pic)
	my_lab.image = my_pic

def change_click(event):
	my_pic = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
	my_lab.config(image=my_pic)
	my_lab.image = my_pic

def change_click2(event):
	my_pic = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
	my_lab.config(image=my_pic)
	my_lab.image = my_pic

def change_click3(event):
	my_pic = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
	my_lab.config(image=my_pic)
	my_lab.image = my_pic

my_pic = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
my_lab = Label(scr,image = my_pic)
# my_lab = Button(scr,image = my_pic)
my_lab.pack(pady = 20,padx = 20)

my_lab.bind("<Enter>",change)
# my_lab.bind("<Leave>",change_back)
my_lab.bind("<Button-2>",change_click)
my_lab.bind("<Button-3>",change_click2)
my_lab.bind("<Double 3>",change_click3)

scr.mainloop()
