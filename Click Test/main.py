import tkinter as tk
import time

class ClickTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Test")
        self.clicks = 0
        self.duration = 10  # Duration of the click test in seconds

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Click as many times as you can in 10 seconds!", font=("Arial", 12))
        self.info_label.pack(padx=20, pady=10)

        self.click_button = tk.Button(self.root, text="Click Me!", command=self.increment_clicks)
        self.click_button.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)

    def increment_clicks(self):
        self.clicks += 1

    def start_test(self):
        self.clicks = 0
        self.click_button.config(state=tk.NORMAL)  # Enable the button
        self.start_button.config(state=tk.DISABLED)  # Disable the start button during the test

        self.root.after(self.duration * 1000, self.end_test)  # Run end_test after duration

    def end_test(self):
        self.click_button.config(state=tk.DISABLED)  # Disable the button after the test ends
        self.start_button.config(state=tk.NORMAL)  # Enable the start button
        result_text = f"Total Clicks: {self.clicks} in {self.duration} seconds!"
        self.info_label.config(text=result_text)

def main():
    root = tk.Tk()
    game = ClickTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
