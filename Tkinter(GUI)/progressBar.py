from tkinter import *
from tkinter import ttk
import time

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def step():
	# my_progress['value'] += 20
	my_progress.start(1)

def step2():		
	my_progress.stop()


my_progress = ttk.Progressbar(scr,orient = HORIZONTAL,	length = 300 ,mode = 'indeterminate')
my_progress.pack(pady = 20)

my_button = Button(scr,text = "Progress",command = step)
my_button.pack(pady = 20)

my_button2 = Button(scr,text = "Stop",command = step2)
my_button2.pack(pady = 20)

scr.mainloop()
