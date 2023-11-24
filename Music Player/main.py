import pygame
import os

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def main():
    pygame.init()
    print("Simple Music Player")
    print("Available songs:")

    # Provide the path to your music directory
    music_directory = "Music"

    # List all music files in the directory
    songs = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]

    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")

    while True:
        try:
            choice = int(input("Enter the song number to play (or 0 to exit): "))
            if choice == 0:
                break
            elif 0 < choice <= len(songs):
                selected_song = os.path.join(music_directory, songs[choice - 1])
                play_music(selected_song)
                while pygame.mixer.music.get_busy():
                    continue  # Wait for music to finish playing
            else:
                print("Invalid choice. Please enter a valid song number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
