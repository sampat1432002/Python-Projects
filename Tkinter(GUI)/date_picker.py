from tkinter import *
from tkcalendar import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

cal = Calendar(scr,selectmode = "day" ,year = 2020,month = 5,day = 22)
cal.pack(pady = 20)

def grab_date():
	my_lab.config(text = cal.get_date())

my_button = Button(scr,text = "Get Date",command = grab_date)
my_button.pack()

my_lab = Label(scr,text = "")
my_lab.pack()

scr.mainloop()