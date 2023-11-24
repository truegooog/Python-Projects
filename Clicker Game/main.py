import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 24))
        self.score_label.pack(padx=20, pady=10)

        self.click_button = tk.Button(self.root, text="Click Me!", command=self.increment_score)
        self.click_button.pack(pady=20)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_score)
        self.reset_button.pack(pady=5)

    def increment_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def reset_score(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

def main():
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
