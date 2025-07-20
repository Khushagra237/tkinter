import tkinter as tk

# Create the main window

root = tk.Tk()

root.title("Tkinter Example")

# Create a label widget

label = tk.Label(root, text="Hello, Tkinter!")

label.pack()

# Run the application

root.mainloop()