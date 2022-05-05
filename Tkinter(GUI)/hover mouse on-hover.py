
from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")


def button_hover_leave(e):
	my_btn["bg"] = "SystemButtonFace"
	status_lab.config(text = "I am departed") 

def button_hover(e):
	my_btn["bg"] = "white"
	status_lab.config(text = "I am hovered over...")


my_btn = Button(scr,text="Click me",font=("Helvatica",28))
my_btn.pack(pady = 50)

status_lab = Label(scr,text="test",bd = 1,relief = SUNKEN,anchor = E)
status_lab.pack(fill = X,side = BOTTOM,ipady = 2)


my_btn.bind("<Enter>",button_hover)
my_btn.bind("<Leave>",button_hover_leave)
scr.mainloop()

