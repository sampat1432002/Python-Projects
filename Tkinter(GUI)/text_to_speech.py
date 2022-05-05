from tkinter import *
import pyttsx3

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

def textEntry():
	engine = pyttsx3.init()
	engine.say(ent.get())
	engine.setProperty('rate',150)
	engine.runAndWait()
	ent.delete(0,END) 

ent = Entry(scr,font = ("helvetivca",26))
ent.pack(pady=10,padx = 10)
btn = Button(scr,text = "Speak",command = textEntry)
btn.pack(pady = 10,padx = 5)

scr.mainloop()
