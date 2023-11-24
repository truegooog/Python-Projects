import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame
pygame.init()

# Function to play music
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# GUI setup
root = tk.Tk()
root.title("GooG Music Player")
root.geometry("125x125")
root.configure(bg='#121212')

# Customizing fonts and colors for a vintage look
button_bg = '#4e4e4e'
button_fg = '#e6e6e6'
label_font = ('Courier', 12)
button_font = ('Courier', 10, 'bold')

play_button = tk.Button(root, text="Play", command=play_music, bg=button_bg, fg=button_fg, font=button_font)
play_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_music, bg=button_bg, fg=button_fg, font=button_font)
stop_button.pack(pady=10)

root.mainloop()
