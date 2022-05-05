from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def info():
	d_lab = Label(scr,text = scr.winfo_geometry())
	d_lab.pack(pady = 20)

	h_lab = Label(scr,text = "Height : " + str(scr.winfo_height()) )
	h_lab.pack(pady = 20)

	w_lab = Label(scr,text = "Width : " + str(scr.winfo_width()) )
	w_lab.pack(pady = 20)

	x_lab = Label(scr,text = "Height : " + str(scr.winfo_x()) )
	x_lab.pack(pady = 20)

	y_lab = Label(scr,text = "Width : " + str(scr.winfo_y()) )
	y_lab.pack(pady = 20)

btn = Button(scr,text = "CLick",command = info)
btn.pack(pady = 20)

scr.mainloop()

