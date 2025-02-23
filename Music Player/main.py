from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer 
import os

# Initializing the mixer
mixer.init()

# Creating the main window
main_window = Tk()
main_window.geometry("700x220")
main_window.title("Music Player")
main_window.resizable(0, 0)

# Adding an icon
icon_path = "Collection/Music Player/icon.png" 
icon_image = PhotoImage(file=icon_path)
main_window.iconphoto(False, icon_image)

# Function to scroll the song title
def scroll_title():
    current_text = current_song_var.get()
    new_text = current_text[1:] + current_text[0]
    current_song_var.set(new_text)
    main_window.after(200, scroll_title)

# Function to play the selected song
def play_song(current_song_var: StringVar, playlist_box: Listbox, status_var: StringVar):
    selected_song = playlist_box.get(ACTIVE)
    current_song_var.set(selected_song)
    mixer.music.load(selected_song)
    mixer.music.play()
    status_var.set("Playing")
    scroll_title() 

# Function to stop the music
def stop_song(status_var: StringVar):
    mixer.music.stop()
    status_var.set("Stopped")

# Function to play the next song
def next_song(current_song_var: StringVar, playlist_box: Listbox, status_var: StringVar):
    current_index = playlist_box.curselection()
    if current_index:
        next_index = (current_index[0] + 1) % playlist_box.size() 
        playlist_box.select_clear(0, END)
        playlist_box.select_set(next_index)
        playlist_box.activate(next_index)  
        play_song(current_song_var, playlist_box, status_var)  

# Function to load songs from a selected directory
def load_songs(playlist_box):
    os.chdir(filedialog.askdirectory(title="Select Folder"))
    tracks = os.listdir()
    playlist_box.delete(0, END)  
    for track in tracks:
        playlist_box.insert(END, track)

# Function to pause the music
def pause_song(status_var: StringVar):
    mixer.music.pause()
    status_var.set("Paused")

# Function to resume the music
def resume_song(status_var: StringVar):
    mixer.music.unpause()
    status_var.set("Resumed")

# Color theme settings
background_color = "#1f1f1f"  
foreground_color = "#e0e0e0"  
highlight_color = "#ff4081"   

# Frames for the GUI layout
current_song_frame = LabelFrame(main_window, text="Current Song", bg=background_color, fg=foreground_color, width=400, height=80)
current_song_frame.place(x=0, y=0)

control_buttons_frame = LabelFrame(main_window, text="Control Buttons", bg=background_color, fg=foreground_color, width=400, height=120)
control_buttons_frame.place(y=80)

playlist_frame = LabelFrame(main_window, text="Playlist", bg=background_color, fg=foreground_color)
playlist_frame.place(x=400, y=0, height=200, width=300)

# Variables to store current song and status
current_song_var = StringVar(main_window, value="Not selected")
status_var = StringVar(main_window, value="Not Available")

# Playlist ListBox with scrollbar
playlist_box = Listbox(playlist_frame, font=("Mali-Regular", 11), selectbackground=highlight_color, bg=background_color, fg=foreground_color)
scroll_bar = Scrollbar(playlist_frame, orient=VERTICAL, command=playlist_box.yview)
playlist_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
playlist_box.pack(fill=BOTH, padx=5, pady=5)

# Displaying the current song label
Label(current_song_frame, text="Currently Playing:", bg=background_color, fg=foreground_color, font=("Mali-Regular", 10, "bold")).place(x=5, y=20)
current_song_label = Label(current_song_frame, textvariable=current_song_var, bg=background_color, fg=highlight_color, font=("Mali-Regular", 12), width=25)
current_song_label.place(x=150, y=20)

# Control buttons
button_style = {"bg": highlight_color, "fg": background_color, "font": ("Mali-Regular", 13), "width": 7}
pause_button = Button(control_buttons_frame, text="Pause", command=lambda: pause_song(status_var), **button_style)
pause_button.place(x=15, y=10)

play_button = Button(control_buttons_frame, text="Play", command=lambda: play_song(current_song_var, playlist_box, status_var), **button_style)
play_button.place(x=195, y=10)

resume_button = Button(control_buttons_frame, text="Resume", command=lambda: resume_song(status_var), **button_style)
resume_button.place(x=285, y=10)

next_button = Button(control_buttons_frame, text="Next", command=lambda: next_song(current_song_var, playlist_box, status_var), **button_style)
next_button.place(x=105, y=10)

load_button = Button(control_buttons_frame, text="Load Directory", command=lambda: load_songs(playlist_box), bg=highlight_color, fg=background_color, font=("Mali-Regular", 13), width=35)
load_button.place(x=10, y=55)

# Status label at the bottom
Label(main_window, textvariable=status_var, bg=background_color, fg=foreground_color, font=("Mali-Regular", 9), justify=LEFT).pack(side=BOTTOM, fill=X)

# Run the GUI
main_window.update()
main_window.mainloop()
