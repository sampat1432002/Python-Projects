from tkinter import *
from random import choice,shuffle

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

global score
global x
x = 0
score = 0
if((score - x) > 0):
	score = score - x

my_score = Label(scr,text = f"Score: {score}",font = ("Helvetica",24,"bold"),fg = "green")
my_score.pack(pady = 20)

my_lab = Label(scr,text="",font = ("Helvetica",48))
my_lab.pack();

anEntry = Entry(scr,font = ("Helvetica",20))
anEntry.pack()

my_lab2 = Label(scr,text = "",font = ("Helvetica",20),fg = "Red")
my_lab2.pack()

my_lab3 = Label(scr,text = "",font = ("Helvetica",20))
my_lab3.pack(pady = 20)

def shuffler():
	global x
	x = 0
	my_lab2.config(text = "")
	my_lab3.config(text = "")
	anEntry.delete(0,END)
	# List of state words
	global states
	states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

	# Pick random state from list
	global word
	word = choice(states)

	# Break apart our chosen word
	break_apart_word = list(word)
	shuffle(break_apart_word)

	# Turn shuffeled list into word
	global shuffled_word
	shuffled_word = ''
	for _ in break_apart_word:
		shuffled_word += _

	# print shuffled word on screen
	my_lab.config(text = shuffled_word)

def check():
	if anEntry.get() in states:
		global score
		score += 10
		my_score.config(text = f"Score: {score}")
		my_lab2.config(text = "Well Done!")
	else:
		my_lab2.config(text = "Sorry, Try Again!")

def answer():
	my_lab2.config(text = word)


def hint(a):
	global x
	x = a
	print(x)
	if(x < len(word)):
		my_lab3.config(text = my_lab3["text"] + " " + word[a])
		x += 1

btn_frm = Frame(scr)
btn_frm.pack(pady = 20)

my_btn = Button(btn_frm,text="Pick Another Word",command = shuffler)
my_btn.grid(row =0,column = 0,padx = 10)

my_btn2 = Button(btn_frm,text="Check",command = check)
my_btn2.grid(row =0,column = 1,padx = 10)

my_btn3 = Button(btn_frm,text="Answer",command = answer,bg = "Green",fg = "white")
my_btn3.grid(row =0,column = 3,padx = 10)

my_btn4 = Button(btn_frm,text="Hint",command = lambda: hint(x),bg = "red")
my_btn4.grid(row =0,column = 2,padx = 10)


shuffler()
scr.mainloop()

