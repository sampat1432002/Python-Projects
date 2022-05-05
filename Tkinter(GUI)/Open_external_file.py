# If you want to open any program directly you have to write its address..
# address = "address of thing we have to open."
# os.system('"%s"' % address)

from tkinter import *
from tkinter import filedialog
import os

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def open_program():
	my_program = filedialog.askopenfilename()
	my_lab.config(text = my_program)
	# Open the Program 
	os.system('"%s"' % my_program)

my_btn = Button(scr,text = "Open Program",command = open_program)
my_btn.pack(pady = 20)

my_lab = Label(scr,text = "")
my_lab.pack(pady = 20)

scr.mainloop()
