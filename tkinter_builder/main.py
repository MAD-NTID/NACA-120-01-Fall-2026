# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("360x240")

        self.label1 = tk.Label(root, text="Username")
        self.label1.place(x=40, y=42, width=80, height=26)

        self.entry1 = tk.Entry(root)
        self.entry1.place(x=140, y=40, width=170, height=28)

        self.label2 = tk.Label(root, text="Password")
        self.label2.place(x=40, y=92, width=80, height=26)

        self.entry2 = tk.Entry(root, show="*")
        self.entry2.place(x=140, y=90, width=170, height=28)

        self.button1 = tk.Button(root, text="Log in", command=self.on_button1)
        self.button1.place(x=140, y=140, width=100, height=34)

        self.label3 = tk.Label(root, text="")
        self.label3.place(x=40, y=190, width=270, height=26)

    def on_button1(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username and password:
            self.label3.configure(text="Welcome, " + username + "!")
        else:
            self.label3.configure(text="Enter a username and password.")
        self.entry2.delete(0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
