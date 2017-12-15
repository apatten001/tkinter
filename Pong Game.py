from tkinter import *
import random
import time

counter = 0
counter1 = 0

tk = Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk,width = 600, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black") #sets the color of the background
canvas.pack()
tk.update()

canvas.create_line(300,0,300,400, fill = "white")

class Ball:
    def __init__(self, canvas, color,paddle,paddle2):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle2 = paddle2
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id,285,185)
        start = [-3,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        pass
        self.canvas.move(self.id,self.x,self.y)
        pos = canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            speed = [1,2,3,4,5]
            random.shuffle(speed)
            self.x = speed[2]
            self.score(True)
        if pos[2] >= self.canvas_width:
            speed2 = [-2,-4]
            random.shuffle(speed2)
            self.x = speed2[0]
            self.score(False)
        if self.hit_paddle(pos) == True:
            pad_speed = [1,2,3,4,5]
            random.shuffle(pad_speed)
            self.x = pad_speed[0]
        if self.hit_paddle2(pos) == True:
            self.x = -3


    def score(self,val):
        global counter
        global counter1

        if val:
            a = self.canvas.create_text(125,40,text = counter,font = ("Arial",60), fill = "white")
            canvas.itemconfig(a, fill = "black")
            counter += 1
            return self.canvas.create_text(125, 40, text=counter, font=("Arial", 60), fill="white")

        if val == False:
            a = self.canvas.create_text(455,40,text = counter1,font = ("Arial",60), fill = "white")
            canvas.itemconfig(a, fill = "black")
            counter1 += 1
            return self.canvas.create_text(455, 40, text=counter1, font=("Arial", 60), fill="white")



    def hit_paddle2(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False


    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if paddle_pos[1] <= pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False




class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,20,100,fill = color) # made paddle
        self.canvas.move(self.id,580,160) # positioned paddle
        self.x = 0 # x and y are the values of the move function
        self.y = 0
        self.canvas_width = self.canvas.winfo_width
        self.canvas_height = self.canvas.winfo_height
        self.canvas.bind_all("<KeyPress-Up>", self.move_up) # binded the left and right key
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        print(pos)
        if pos[0] <= 0: # this tells that we didnt want x to go past 0
            self.x = 0
        if pos[2] >= self.canvas_width():
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height():
            self.y = 0

    def move_up(self, event):
        self.y = -2
    def move_down(self,event):
        self.y = 2


class Paddle2:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(20,100,0,0, fill = color)
        self.canvas.move(self.id,0,200)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-a>", self.move_up)
        self.canvas.bind_all("<KeyPress-z>", self.move_down)
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos2 = self.canvas.coords(self.id)
        print(pos2)
        if pos2[0] <= 0:
            self.x = 0
        if pos2[2] >= self.canvas_width:
            self.x = 0
        if pos2[1] <= 0:
            self.y = 0
        if pos2[3] >= self.canvas_height:
            self.y = 0


    def move_up(self,event):
        self.y = -2
    def move_down(self,event):
        self.y = 2





# gameplay


paddle = Paddle(canvas, "#eb96ff") # which ever is on top in order is the bottom layer
paddle2 = Paddle2(canvas,"#91a7ff")
ball = Ball(canvas,"#00efab",paddle,paddle2)


while 1:

    ball.draw()
    paddle.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)



    # if counter or counter1 == 10:
    #     canvas.create_text(300,150, text = "Game Over", font = ("Arial",60), fill = "red")
    #     time.sleep(1)


tk.mainloop()

