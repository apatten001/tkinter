from tkinter import *

root =  Tk()

def leftClick(event):
    print("left")

def rightClick(event):
    print("right")

def scroll(event):
    print("Scroll")

def leftKey(event):
    print("Left key Pressed")

def rightKey(event):
    print("right key pressed")

def aKey(event):
    print("a key pressed")

root.geometry("500x500")
#sets the windows size

root.bind("<Button-1>", leftClick)

root.bind("<Button-2>", rightClick)

root.bind("<Button-3>", scroll)

root.bind("<Left>", leftKey)

root.bind("<Right>",  rightKey)

root.bind("<a>", aKey)


root.mainloop()