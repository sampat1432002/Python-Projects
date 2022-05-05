from tkinter import *
import time

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def clock():
	hour = time.strftime("%H") 
	minute = time.strftime("%M")
	second = time.strftime("%S")
	
	my__lab.after(1000,clock)
	my__lab.config(text= hour + ":" + minute + ":" + second + " " + time.strftime("%p"))

def update():
	my__lab.config(text = "New Text")
my__lab2 = Label(scr,text = time.strftime("%A") + ", " + time.strftime("%B")  ,font = ("Helvetica",28),fg = "Red")
my__lab2.pack(pady=20)
my__lab= Label(scr,text = "",font = ("Helvetica",48),fg = "Red",bg = "Black")
my__lab.pack(pady=20)
my__lab.after(500,clock)

scr.mainloop()
