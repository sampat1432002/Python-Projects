from tkinter import *
from tkinter import filedialog

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

# Read onl -- r
# Read and Write -- r+
# Write Only -- w (over-written)
# Wirte and Read -- w+ (Over Written)
# Append Only -- a (end of file) 
# Apppend and Read -- a+ (end of file)  

# Create clear fuction
def open_text():
	text_file = filedialog.askopenfilename(initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open Text File",filetypes = (("Text Files","*.txt"),))
	text_file = open(text_file,'r')
	stuff = text_file.read()

	my_text.insert(END,stuff)
	text_file.close()

def save_text():
	text_file = filedialog.askopenfilename(initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open Text File",filetypes = (("Text Files","*.txt"),))
	text_file = open(text_file,'w')
	text_file.write(my_text.get(1.0,END))

my_text = Text(scr,width = 60,height = 20,font = ("Helvetica",14))
my_text.pack(pady = 20)

open_btn = Button(scr,text = "Open Text File",command = open_text)
open_btn.pack(pady = 20)

save_btn = Button(scr,text = "Save",command = save_text)
save_btn.pack(pady = 20)

scr.mainloop()