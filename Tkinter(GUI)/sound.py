
from tkinter import *
import pygame

scr = Tk()
scr.title("Canvas")
scr.iconbitmap("images/google.ico")
scr.geometry("500x600")

pygame.mixer.init()

global e
e = 0

def  play():
	pygame.mixer.music.load("E:/Music/04 new one/Maroon 5 - Memories.mp3")
	pygame.mixer.music.play(loops = 0)

def play_pause(event):
	global e
	if(event == 0):
		e = 1
		pygame.mixer.music.pause()
	else:
		e = 0
		pygame.mixer.music.unpause()

my_btn = Button(scr,text = "Play Song",font = ("Helvetica",32),command = play)
my_btn.pack(pady = 20)

pause_play_btn = Button(scr,text = "Pause/Play",font = ("Helvetica",32),command = lambda: play_pause(e))
pause_play_btn.pack(pady = 20)

scr.mainloop()

