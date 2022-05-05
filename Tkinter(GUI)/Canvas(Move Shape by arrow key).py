from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("google.ico")
scr.geometry("500x500")

w = 600
h = 400
x = w // 2 
y = h //2

my_canvas = Canvas(scr,width = w,height = h,bg = "white")
my_canvas.pack(pady = 20)

my_circle = my_canvas.create_oval(x,y,x+5,y+5,fill = "red")

def left(event):
	x = -10
	y = 0 

	my_canvas.move(my_circle,x,y)

def right(event):
	x = 10 
	y = 0 

	my_canvas.move(my_circle,x,y)

def up(event):
	x = 0 
	y = -10 

	my_canvas.move(my_circle,x,y)

def down(event):
	x = 0 
	y = 10 

	my_canvas.move(my_circle,x,y)

scr.bind("<Left>",left)
scr.bind("<Right>",right)
scr.bind("<Up>",up)
scr.bind("<Down>",down)

scr.mainloop()