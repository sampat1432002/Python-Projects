from tkinter import *
from tkinter import filedialog
import os

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def grab():
	my_lab.config(text = my_spin.get())

# my_spin = Spinbox(scr,from_ = 0,to = 100,increment = 1,font= ("Helvetica"))
my_spin = Spinbox(scr,values = ("John","Tim","Mary","Tina"),increment = 1,font= ("Helvetica"))
my_spin.pack(pady =20)

my_btn = Button(scr,text = "Submit",command = grab)
my_btn.pack(pady = 20)

my_lab = Label(scr,text = "")
my_lab.pack(pady =  20)

scr.mainloop()