from tkinter import *
import time

root= Tk()

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

canvas.create_rectangle(10,20,30,60)
for i in range(0,100):
    canvas.move(1,5,2)# moving object id 1. th specify how many times in (x 5 pixels to right,y 2 to bottom)
    root.update() # updates the canvas in case of changes
    time.sleep(0.05) #makes the change sleep 5 tenths of a sec


root.mainloop()