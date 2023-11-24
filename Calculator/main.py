import tkinter as tk

def on_click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "+",
    "C", "="
]

row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, padx=30, pady=20, command=lambda key=button: on_click(key)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
