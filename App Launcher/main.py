import tkinter as tk
from tkinter import filedialog
import subprocess

def add_app():
    filepath = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if filepath:
        app_listbox.insert(tk.END, filepath)

def remove_app():
    selected_index = app_listbox.curselection()
    if selected_index:
        app_listbox.delete(selected_index)

def run_selected():
    selected_index = app_listbox.curselection()
    if selected_index:
        selected_app = app_listbox.get(selected_index)
        subprocess.Popen(selected_app)

def save_apps():
    with open("saved_apps.txt", "w") as file:
        apps = app_listbox.get(0, tk.END)
        for app in apps:
            file.write(app + "\n")

def load_apps():
    try:
        with open("saved_apps.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                app_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("App Launcher")

app_listbox = tk.Listbox(root, width=50)
app_listbox.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Add App", command=add_app)
add_button.pack()

remove_button = tk.Button(root, text="Remove Selected", command=remove_app)
remove_button.pack()

run_button = tk.Button(root, text="Run Selected", command=run_selected)
run_button.pack()

save_button = tk.Button(root, text="Save Apps", command=save_apps)
save_button.pack()

load_apps()

root.mainloop()
