import main
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def save():
    global scrolltext
    text = scrolltext.get("1.0", END)
    file = open("files/text.txt", "w")
    file.write(text)
    file.close()
def load():
    global scrolltext
    try:
        file = open("files/text.txt", "r")
        text = file.read()
        file.close()
        scrolltext.insert(INSERT, text)
    except:
        pass

app = main.App()
window = app.window()
text = Button(window, text="Save", command=save)
text.place(x=0, y=25, width=100)
text = Button(window, text="Load", command=load)
text.place(x=100, y=25, width=100)

scrolltext = ScrolledText(window)
scrolltext.place(x=0, y=50, width=200, height=150)

window.configure(width=200, height=200)