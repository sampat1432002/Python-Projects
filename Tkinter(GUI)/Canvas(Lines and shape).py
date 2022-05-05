from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("google.ico")
scr.geometry("500x500")

my_canvas = Canvas(scr,width = 300,height = 200,bg = "white")
my_canvas.pack(pady = 20)

 # my_canvas.create_rectangle(x1,y1,x2,y2,fill = "color")
 # x1,y1 : Top left 
 # x2,y2 : Bottom right 
my_canvas.create_rectangle(20,180,280,20, fill = "wheat")


# Create Oval
 # x1,y1 : Top left 
 # x2,y2 : Bottom right 
my_canvas.create_oval(20,180,280,20, fill = "deep skyblue")

# Create Line
# my_canvas.create_line(x1,y1,x2,y2,fill = "color")
my_canvas.create_line(0,100,300,100,fill = "red")
my_canvas.create_line(150,0,150,200,fill = "blue")

scr.mainloop()