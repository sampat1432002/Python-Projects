from tkinter import *

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

# Creating frame and scrollba
frm = Frame(scr)
my_scrollbar = Scrollbar(frm,orient = VERTICAL)

# Listbox
# SINGLE,BORWSE,MULTIPLE,EXTENDED
my_listbox = Listbox(frm,width = 50,yscrollcommand = my_scrollbar.set)

# configure.scrollbar
my_scrollbar.config(command = my_listbox.yview)
my_scrollbar.pack(side = RIGHT,fill  = Y)
frm.pack()

my_listbox.pack(pady = 15)

# Add item to listbox
my_listbox.insert(END,"This is a item")
my_listbox.insert(END,"Second!")

# Add list f items 
my_list = ["one","Two","Three","one","Two","Three","one","Two","Three","one","Two","Three","one","Two","Three"]

for item in my_list:
	my_listbox.insert(END,item)

def delete():
	my_listbox.delete(ANCHOR)
	my_label.config(text = '')

def select():
	my_label.config(text = my_listbox.get(ANCHOR))


def delete_all():
	my_listbox.delete(0,END)
my_btn = Button(scr,text = "Delete",command = delete)
my_btn.pack(pady = 10)

my_btn2 = Button(scr,text = "Select",command = select)
my_btn2.pack(pady = 10)	

global my_label
my_label = Label(scr,text = '')
my_label.pack(pady = 5)

my_btn2 = Button(scr,text = "Delete All",command = delete_all)
my_btn2.pack(pady = 10)	

scr.mainloop()