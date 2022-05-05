from tkinter import *
from tkinter import filedialog
from tkinter import font 
# from PIL import tk,ImageTk,Image

scr = Tk()
scr.title("Textpad")
scr.iconbitmap("images/google.ico")
scr.geometry("1200x700")

# Set variable for open file name 
global open_status_name
open_status_name = False

global selected
selected = False
# Create New File Function
def new_file():
	# Delete pretextes
	my_text.delete("1.0",END)
	# Update the status bar
	scr.title('Untitled - TextPad')
	status_bar.config(text = "New File         ")

	# Set variable for open file name 
	global open_status_name
	open_status_name = False

# Create New File Function
def open_file():
	# Delete pretextes
	my_text.delete("1.0",END)
	
	# Grab Filename 
	text_file = filedialog.askopenfilename(initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open File",filetypes = (("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
	
	# Check to see if there is a file name
	if text_file:
		# Make File Name Global we can access
		global open_status_name
		open_status_name = text_file


	# Update Status Bar
	name  = text_file
	status_bar.config(text = f'{name}         ')
	name = name.replace("D:/Sampat.py/Tkinter(GUI)/","")
	scr.title(f'{name} - TextPad')

	# Open the File
	text_file = open(text_file,'r')
	stuff = text_file.read()

	# Add file to textbox
	my_text.insert(END,stuff)

	# Close the file
	text_file.close()

# Create Save as File
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension = ".*",initialdir = "D:/Sampat.py/Tkinter(GUI)/",title = "Open File",filetypes = (("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*"))) 
	if text_file:
		# Update Staus Bar
		name = text_file
		status_bar.config(text = f'Saved : {name}         ')
		name = name.replace("D:/Sampat.py/Tkinter(GUI)/","")
		scr.title(f'{name} - TextPad')

		# Save the file
		text_file = open(text_file,"w")
		text_file.write(my_text.get(1.0,END))

		# Close the file
		text_file.close()

def save_file():
	global open_status_name
	if open_status_name:
		# Save the file
		text_file = open(open_status_name,"w")
		text_file.write(my_text.get(1.0,END))

		# Close the file
		text_file.close()

		status_bar.config(text = f'Saved : {open_status_name}         ')

	else:
		save_as_file()

# Cut Text
def cut_text(e):
	global selected
	if e:
		selected = scr.clipboard_get()
	else:
		if my_text.selection_get():
			# Grab selected textfrom text box
			selected = my_text.selection_get()
			#Delete slectd text from text box 
			my_text.delete("sel.first","sel.last")
			# Clear the clipboard and append 
			scr.clipboard_clear()
			scr.clipboard_append(selected)

# Copy Text
def copy_text(e):
	global selected
	if e:
		selected = scr.clipboard_get()

	if my_text.selection_get():
		#  Grab selected text from text box
		selected = my_text.selection_get()
		scr.clipboard_clear()
		scr.clipboard_append(selected)

# Paste Text
def paste_text(e):
	global selected
	if e:
		selected = my_text.selection_get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position,selected)

# Create Frame
my_frm = Frame(scr)
my_frm.pack(pady = 5)

# Create our Scrollbar for the text box
text_scroll = Scrollbar(my_frm)
text_scroll.pack(side = RIGHT,fill = Y)

# Create Text Box
my_text = Text(my_frm,width = 97,height = 25,font = ("Helvetica",16),selectbackground = "yellow",selectforeground = "black",undo = True,yscrollcommand = text_scroll.set)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command = my_text.yview())

# Create Menu
my_menu = Menu(scr)
scr.config(menu =  my_menu)

# Add File Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File",menu = file_menu)

file_menu.add_cascade(label = "New",command = new_file)
file_menu.add_cascade(label = "Open",command = open_file)
file_menu.add_cascade(label = "Save",command = save_file)
file_menu.add_cascade(label = "Save as",command = save_as_file)
file_menu.add_separator()
file_menu.add_cascade(label = "Exit")

# Add Edit Menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit",menu = edit_menu)

edit_menu.add_cascade(label = "Cut",command = lambda: cut_text(False))
edit_menu.add_cascade(label = "Copy",command = lambda: copy_text(False))
edit_menu.add_cascade(label = "Paste",command = lambda: paste_text(False))
edit_menu.add_cascade(label = "Undo")
edit_menu.add_cascade(label = "Redo")

# Add Status Bar TO Bottom Of App
status_bar = Label(scr,text = "Ready         ",anchor = E)
status_bar.pack(fill = X,side = BOTTOM,ipady = 5)

# Edit Binding
scr.bind('<Control-Key-x>',cut_text)
scr.bind('<Control-Key-c>',copy_text)
scr.bind('<Control-Key-v>',paste_text)

scr.mainloop()
