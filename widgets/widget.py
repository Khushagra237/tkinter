from cProfile import label
import tkinter as tk
from datetime import date

# Create the main window

root = tk.Tk()

root.title("Getting started with Widgets")

# Create a label widget

lbl = tk.Label(root, text="Hello, Tkinter!")
bg= "lightblue"

name_lbl = tk.Label(text = "Full Name", bg = "#3895D3")
name_entry = tk.Entry()
def display():
    name = name_entry.get()

    global message
    message = "Welcome to the application! \nToday's date is:"
    greet = "Hello, " + name + "\n"
    text_box.insert(tk.END , greet)
    text_box.insert(tk.END , message)
    text_box.insert(tk.END , date.today())

text_box = tk.Text(height=3)
btn = tk.Button(text="Begin", command=display, height=1)
btn.configure(bg="#1261A0", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()

# Run the application

root.mainloop()