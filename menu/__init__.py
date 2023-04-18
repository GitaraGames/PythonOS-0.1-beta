import main
from tkinter import *

app = main.MainMenu()
window = app.window()

# Example
button_notepad = Button(window, text="Notepad", command=lambda:exec(open("Notepad/__init__.py", "r").read()))
button_notepad.pack()

button_shutdown = Button(window, text="Shutdown", command=lambda:exit())
button_shutdown.pack()