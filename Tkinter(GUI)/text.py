from tkinter import *
from tkinter import filedialog
from tkinter import font 
# from PIL import tk,ImageTk,Image

scr = Tk()
scr.title("Textpad")
scr.iconbitmap("images/google.ico")
scr.geometry("500x800")

# Read onl -- r
# Read and Write -- r+
# Write Only -- w (over-written)
# Wirte and Read -- w+ (Over Written)
# Append Only -- a (end of file) 
# Apppend and Read -- a+ (end of file)  

# Create clear fuction
def clear():
	my_text.delete(1.0,END)

# Create clear fuction
def open_text():
	text_file = filedialog.askopenfilename(initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open Text File",filetypes = (("Text Files","*.txt"),))
	
	name = text_file
	text_file = open(text_file,'r')
	stuff = text_file.read()

	my_text.insert(END,stuff)
	text_file.close()

	name = name.replace("D:/Sampat.py/Tkinter(GUI)/","")
	name = name.replace(".txt","")

	scr.title(f'{name} - Textpad')

def save_text():
	text_file = filedialog.askopenfilename(initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open Text File",filetypes = (("Text Files","*.txt"),))
	text_file = open(text_file,'w')
	text_file.write(my_text.get(1.0,END))

def add_img():
	# Add Image
	global my_image
	my_img = PhotoImage(file = 'D:/Sampat.py/Tkinter(GUI)/Images/shuffle_disabled.png')
	position = my_text.index(INSERT)
	my_text.image_create(position,image = my_img)

def select():
	selected = my_text.selection_get()
	# my_lab.config(text = selected)

def bold_text():
	bold_font = font.Font(my_text,my_text.cget("font"))
	bold_font.configure(weight = "bold") 

	my_text.tag_configure("bold",font = bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold","sel.first","sel.last")

	else :
		my_text.tag_add("bold","sel.first","sel.last")

def italic_text():
	italic_font = font.Font(my_text,my_text.cget("font"))
	italic_font.configure(slant = "italic") 

	my_text.tag_configure("italic",font = italic_font)

	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic","sel.first","sel.last")

	else :
		my_text.tag_add("italic","sel.first","sel.last")

my_frame = Frame(scr) 
my_frame.pack(pady = 20)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT,fill = Y)

my_text = Text(my_frame,width = 60,height = 20,font = ("Helvetica",14), selectbackground = "yellow",selectforeground = "black",yscrollcommand = text_scroll.set,undo = True)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command = my_text.yview)

open_btn = Button(scr,text = "Open Text File",command = open_text)
open_btn.pack(pady = 5)

save_btn = Button(scr,text = "Save",command = save_text)
save_btn.pack(pady = 5)

select_btn = Button(scr,text = "Select Text",command = select)
select_btn.pack(pady = 5)

bold_btn = Button(scr,text = "Bold",command = bold_text)
bold_btn.pack(pady = 5) 

italic_btn = Button(scr,text = "Italic",command = italic_text)
italic_btn.pack(pady = 5)

image_btn = Button(scr,text = "Add Image",command = add_img)
image_btn.pack(pady = 5)

my_lab =  Label(scr,text = "")
my_lab.pack()

clear_btn = Button(scr,text = "Clear",command= clear)
clear_btn.pack(pady = 5)

undo_btn = Button(scr,text = "Undo",command = my_text.edit_undo)
undo_btn.pack(pady = 5)

redo_btn = Button(scr,text = "Redo",command = my_text.edit_undo)
redo_btn.pack(pady = 5)
scr.mainloop()