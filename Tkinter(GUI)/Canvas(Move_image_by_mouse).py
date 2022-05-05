from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

w = 600
h = 400
x = w // 2 
y = h //2

my_canvas = Canvas(scr,width = w,height = h,bg = "white")
my_canvas.pack(pady = 20)

# Add image to canvas
img = PhotoImage(file = "images/stick_man.png")
my_img = my_canvas.create_image(0,0,anchor = NW,image=img)

def move(e):
	# e.x  
	# e.y  
	global img
	img = PhotoImage(file = "images/stick_man.png")
	my_img = my_canvas.create_image(e.x,e.y,image=img)
	my_lab.config(text = "Coordinates\n x: " + str(e.x) + " y: " +str(e.y))


# scr.bind("<Left>",left)
# scr.bind("<Right>",right)
# scr.bind("<Up>",up)
# scr.bind("<Down>",down)
my_lab = Label(scr,text = "")
my_lab.pack(pady = 20)

my_canvas.bind('<B1-Motion>',move)

scr.mainloop()