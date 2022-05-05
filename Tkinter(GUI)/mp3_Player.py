from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from mutagen.mp3 import MP3
import random
import time
import tkinter.ttk as ttk
import pygame


scr = Tk()
scr.title("MP3 Player")
scr.iconbitmap("Images/MP3 Player.ico")
scr.geometry("700x700")
scr.config(bg = "white")

# Initiating pygame mixer
pygame.mixer.init()

# Creatisng Menu
fun_column = Menu(scr)
scr.config(menu = fun_column)

# Creating frame and scrollba
master_frm = Frame(scr,bg = "white")
frm = Frame(master_frm)

x_scrollbar = Scrollbar(frm,orient = HORIZONTAL)
y_scrollbar = Scrollbar(frm,orient = VERTICAL)

# Listbox (SINGLE,BORWSE,MULTIPLE,EXTENDED)
my_listbox = Listbox(frm,height = 20,width = 90,bd = 5,yscrollcommand = y_scrollbar.set,xscrollcommand = x_scrollbar.set,bg = "Black",fg = "White",selectmode = SINGLE,selectbackground = "grey")

# configure.scrollbar
x_scrollbar.config(command = my_listbox.xview)
x_scrollbar.pack(side = BOTTOM,fill  = X)
y_scrollbar.config(command = my_listbox.yview)
y_scrollbar.pack(side = RIGHT,fill  = Y)

frm.grid(row = 0,column = 0,columnspan = 2)
master_frm.pack()

my_listbox.pack()

global play_list
global playlist_main
playlist_main = []
# Creating Playlist
play_list = [
			]

for i in play_list:
	my_listbox.insert(END,i)

playlist_main = my_listbox.get(0,END)

# Openning Images
vol_img = ImageTk.PhotoImage(Image.open("Images/vol.png").resize((35,35),Image.ANTIALIAS))
shuffle_img = ImageTk.PhotoImage(Image.open("Images/shuffle.png").resize((35,35),Image.ANTIALIAS))
shuffle_disabled_img = ImageTk.PhotoImage(Image.open("Images/shuffle_disabled.png").resize((35,35),Image.ANTIALIAS))
play_img = ImageTk.PhotoImage(Image.open("Images/play.png").resize((70,70),Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open("Images/pause.png").resize((70,70),Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open("Images/stop.png").resize((35,35),Image.ANTIALIAS))
previous_img = ImageTk.PhotoImage(Image.open("Images/prev.png").resize((35,35),Image.ANTIALIAS))
next_img = ImageTk.PhotoImage(Image.open("Images/next.png").resize((35,35),Image.ANTIALIAS))

global e
global flag 
global shuffle_check
shuffle_check = 0 
flag = 1
e = 2

global song_check
song_check = ""

def play_time():
	global my_slider
	global song_len
	global current_time
	# Current time of played song
	current_time = (pygame.mixer.music.get_pos()  // 1000)
	
	conv_current_time = time.strftime('%M:%S',time.gmtime(current_time))

	# Importing song title
	song = my_listbox.get(ACTIVE)
	song = f"E:/Music/04 new one/{song}.mp3"

	# Load Song with Mutagen
	song_mut = MP3(song_check) 

	# Get Song Length with mutagen
	song_len = int(song_mut.info.length)

	# Convert to time Formate
	conv_song_len = time.strftime('%M:%S',time.gmtime(song_len))

	if int(my_slider.get()) == int(song_len):
		# DISPLAY
		status_bar1.config(text = f"{conv_song_len} / {conv_song_len}")
		# Next song if the current song end in the pause button
		next_m()
		pass
	elif(e == 1):
		pass

	elif(int(my_slider.get())) == int(current_time):
		# Slider hasn't been moved

		# Update Slider To Position			
		my_slider.config(to = song_len,value = current_time)

	else:
		# Slider has been moved
		if(e == 0):
			# Update Slider To Position			
			my_slider.config(to = song_len,value = int(my_slider.get()))

			conv_current_time = time.strftime('%M:%S',time.gmtime(int(my_slider.get())))

			# DISPLAY
			status_bar1.config(text = f"{conv_current_time}")
			status_bar2.config(text = f"{conv_song_len}")
			# Move this thing along by one sec
			next_time = int(my_slider.get()) + 1
			my_slider.config(value = next_time)  

	# Update Time
	status_bar1.after(1000,play_time)

def prev_m():
	global e
	global song_check

	# Getting current song number
	next_song = my_listbox.curselection()
	try:
		next_song = next_song[0] - 1   # Decrementing
	except:
		return

	# Importing song title
	song = my_listbox.get(next_song)

	song = f"E:/Music/04 new one/{song}.mp3"

	if(e == 0):	
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(loops = 0)
		# Saving song footprint
		song_check = song

	my_slider.config(value = 0)
	current_time = int(my_slider.get())
	# Load Song with Mutagen
	song_mut = MP3(song) 
	# Get Song Length with mutagen
	song_len = int(song_mut.info.length)
	# Convert to time Formate
	conv_song_len = time.strftime('%M:%S',time.gmtime(song_len))
	# DISPLAY
	status_bar1.config(text = "00:00")
	status_bar2.config(text = f"{conv_song_len}")

	# Selecting the other song AND clearing the current selection
	my_listbox.selection_clear(ACTIVE)
	my_listbox.activate(next_song)

	# Setting up the selection
	my_listbox.selection_set(next_song,last = None)

def next_m():
	global e
	global song_check

	# Getting current song number
	next_song = my_listbox.curselection()
	next_song = next_song[0] + 1   # Incrementing

	# Importing song title
	song = my_listbox.get(next_song)

	song = f"E:/Music/04 new one/{song}.mp3"
		
	if(e == 0):	
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(loops = 0)
		# Saving song footprint
		song_check = song 

	my_slider.config(value = 0)
	current_time = int(my_slider.get())
	# Load Song with Mutagen
	song_mut = MP3(song) 
	# Get Song Length with mutagen
	song_len = int(song_mut.info.length)
	# Convert to time Formate
	conv_song_len = time.strftime('%M:%S',time.gmtime(song_len))
	# DISPLAY
	status_bar1.config(text = "00:00")
	status_bar2.config(text = f"{conv_song_len}")

	# Selecting the other song AND clearing the current selection
	my_listbox.selection_clear(ACTIVE)
	my_listbox.activate(next_song)

	# Setting up the selection
	my_listbox.selection_set(next_song,last = None)

# Create shuffle and loop button function
def shuffle_loop():
	global e
	song = my_listbox.get(ACTIVE)
	# Taking the list from listbox
	lst = list(my_listbox.get(0,END))
	my_listbox.delete(0,END)
	shuffle_loop_btn["image"] = shuffle_img
	random.shuffle(lst)
	lst.remove(song)

	for i in lst:	
		my_listbox.insert(0,i)
	my_listbox.insert(0,song)
	if(pygame.mixer.music.get_busy):
		# Setting up the selection
		my_listbox.activate(0)
		my_listbox.selection_set(0,last = None)
		e = 0

def play_pause(event):
	global e
	global song_check

	sample = my_listbox.get(0,END)
	if(sample == ()):
		return

	song = my_listbox.get(ACTIVE)
	song = f"E:/Music/04 new one/{song}.mp3"

	#  To pause the music
	if(event == 0):
		# Changing the icon
		play_pause_btn["image"] = play_img
		e = 1
		pygame.mixer.music.pause()
	# To play the music
	elif(event == 1):
		e = 0
		# Changing icon
		play_pause_btn["image"] = pause_img
		if(song == song_check):
			pygame.mixer.music.unpause()
		else:
			my_slider.config(value = 0)
			current_time = int(my_slider.get())
			pygame.mixer.music.load(song)
			pygame.mixer.music.play(loops = 0)
			song_check = song
		# Getting the play time
		play_time()
	
	# To initialize the music
	elif(event == 2):
		e = 0
		my_slider.config(value = 0)
		current_time = int(my_slider.get())	
		song_check = song
		play_pause_btn["image"] = pause_img
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(loops = 0)
		
		# Setting up the selection
		my_listbox.activate(0)
		my_listbox.selection_set(0,last = None)

		# Getting the play time
		play_time()

def stop_m():
	global e
	e = 1
	play_pause_btn["image"] = play_img
	pygame.mixer.music.stop()
	my_slider.config(value = 0)
	my_listbox.selection_clear(ACTIVE)
	status_bar1.config(text = "00:00")
	status_bar2.config(text = "00:00")


# Crate delete a song 
def delete_a_song():
	cur_selection = my_listbox.curselection()
	if(cur_selection == song_check):
		pygame.mixer.music.stop()
		my_slider.config(value = 0)
		stop_m()
	my_listbox.delete(cur_selection,last = None)

# Create delete all songs
def delete_all_songs():
	my_slider.config(value = 0)
	my_listbox.delete(0,END)
	stop_m()

def add_a_song():
	global flag
	global playlist_main
	if (flag == 1):
		delete_all_songs()
	song = filedialog.askopenfilename(initialdir = 'E:/Music/04 new one',title = 'Find a Song',filetypes = (('mp3 Files','*.mp3'), ))
	# Trimming the music file name
	song = song.replace("E:/Music/04 new one/","")
	song = song.replace(".mp3","")
	my_listbox.insert(0,song)
	flag = 0
	playlist_main = my_listbox.get(0,END)

def add_many_songs():
	global flag
	global e
	if (flag == 1):
		delete_all_songs()
		# Changing icon
		play_pause_btn["image"] = play_img
		e = 2

	songs = filedialog.askopenfilenames(initialdir = 'E:/Music/04 new one',title = 'Find a Song',filetypes = (('mp3 Files','*.mp3'), ))
	
	# Trimming the music file name
	for song in songs:
		song = song.replace("E:/Music/04 new one/","")
		song = song.replace(".mp3","")
		
		# Insert in Listbox
		my_listbox.insert(END,song)
	flag = 0
	playlist_main = my_listbox.get(0,END)

def saved_songs():
	global e
	global flag
	flag = 1
	e = 2
	for i in play_list:
		my_listbox.insert(END,i)
	playlist_main = my_listbox.get(0,END)

def slide(x):
	song = my_listbox.get(ACTIVE)
	song = f"E:/Music/04 new one/{song}.mp3"
	
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops = 0,start = int(my_slider.get()))

global vol_widget_check
vol_widget_check = False
def change_vol(x):
	pygame.mixer.music.set_volume((float)((vol_slider.get())/100))

def vol():
	global vol_widget_check
	if vol_widget_check:
		vol_slider.grid_forget()
		vol_widget_check = False

	else:
		vol_slider.grid(row = 0,column = 1,columnspan = 2,pady = 10,sticky = W)
		vol = (int)(pygame.mixer.music.get_volume() * 100)
		vol_slider.config(value = vol)
		vol_widget_check = True

# Add songs menu
add_song_menu = Menu(fun_column)
fun_column.add_cascade(label = "Create Playlist",menu = add_song_menu)
add_song_menu.add_command(label = "Add a Song" , command = add_a_song)
add_song_menu.add_command(label = "Add Many Songs" , command = add_many_songs)
add_song_menu.add_command(label = "Saved List" , command = saved_songs)

# Create Remove Song Menu
remove_song_menu = Menu(fun_column)
fun_column.add_cascade(label = "Remove Songs",menu = remove_song_menu)
remove_song_menu.add_cascade(label = "Delete a Song",command = delete_a_song)
remove_song_menu.add_cascade(label = "Delete all Songs",command = delete_all_songs)

# Function Frame
function_frame = Frame(scr,bg = "white")
function_frame.pack(pady = 20)

# Volume Button
vol_btn = Button(function_frame,image = vol_img,command = vol,bg = "white",bd = 0,height = 70,width = 70)
vol_btn.grid(row = 0,column = 0,pady = 10)

# Create Volume Slider
vol_slider = ttk.Scale(function_frame,from_ = 0,to = 100,orient = HORIZONTAL,length = 150,value = 0,command = change_vol)

# Create Status Bar
status_bar1 = Label(function_frame,text ="00:00",bd = 0,font = ("Bold"),bg = "white")
status_bar1.grid(row = 1,column = 0,pady = 10)

# Create Music Position Slider
my_slider = ttk.Scale(function_frame,from_ = 0,to = 100,orient = HORIZONTAL,length = 450,value = 0,command = slide)
my_slider.grid(row = 1,column = 1,columnspan = 3,pady = 10)

# Create Status Bar
status_bar2 = Label(function_frame,text ="00:00",bd = 0,font = ("Bold"),bg = "white")
status_bar2.grid(row = 1,column = 4,pady = 10)

# Previous Music Button
shuffle_loop_btn = Button(function_frame,image = shuffle_img,command = shuffle_loop,bg = "white",bd = 0,height = 70,width = 70)
shuffle_loop_btn.grid(row = 2,column = 0,padx = 30,pady = 10)

# Previous Music Button
previous_btn = Button(function_frame,image = previous_img,command = prev_m,bg = "white",bd = 0,height = 70,width = 70)
previous_btn.grid(row = 2,column = 1,padx = 30,pady = 10)

# Play/Pause Button
play_pause_btn = Button(function_frame,image = play_img,command = lambda:play_pause(e),bg = "white",bd = 0,height = 70,width = 70)
play_pause_btn.grid(row = 2,column = 2,padx = 30,pady = 10)

# Next Music Button
next_btn = Button(function_frame,image = next_img,command = next_m,bg = "white",bd = 0,height = 70,width = 70)
next_btn.grid(row = 2,column = 3,padx = 30,pady = 10)

# Stop Music Button
stop_btn = Button(function_frame,image = stop_img,command = stop_m,bg = "white",bd = 0,height = 70,width = 70)
stop_btn.grid(row = 2,column = 4,pady = 10)


scr.mainloop()