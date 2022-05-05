from tkinter import *
import time
from random import randint
import threading

scr = Tk()
scr.title("Canvas")
scr.geometry("500x600")

def five_sec():
	time.sleep(5)
	my_label.config(text = '5 sec up')

def rando():
	my_label.config(text = f'Random Number: {randint(1,100)}')

my_label = Label(scr,text = "Hello There!")
my_label.pack(pady = 20)

my_btn2 = Button(scr,text = "5_sec",command=threading.Thread(target=five_sec).start()) 
my_btn2.pack(pady = 10)

my_btn1 = Button(scr,text = "Pick Random Number",command=rando) 
my_btn1.pack(pady = 10)



scr.mainloop()
