from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def geo():
	w = width_entry.get()
	h = height_entry.get()
	scr.geometry(f"{w}x{h}")

btn = Button(scr,text ="press",command = geo)
btn.pack(pady = 20)

lab_width = Label(scr,text = "Width")
lab_width.pack()

width_entry = Entry(scr)
width_entry.pack(pady = 20)

lab_height = Label(scr,text = "Height")
lab_height.pack()

height_entry = Entry(scr)
height_entry.pack(pady = 20)
scr.mainloop()

	