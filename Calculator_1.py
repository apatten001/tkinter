from tkinter import *

root= Tk()
root.title("Calculator")
root.maxsize(160,160)

equa = "" # equa is set it back to 0

equation = StringVar() # this updates the text of my label

calculation = Label(root, textvariable = equation) # this updates calculation as well. use test variable

equation.set("enter your equation:")

calculation.grid(columnspan = 4) # this outputs the outcome of our equation

def btnpress(num):
    global equa
    equa = equa + str(num) #keeping what equa had and adding number
    equation.set(equa)

def EqualPress():
    global equa  # you have to use global equa because equas not defined locally
    total = str(eval(equa))
    equation.set(total)
    equa = "" # this sets equa back to original value

def clear():
    global equa
    equa = ""
    equation.set("") # this function allows calculator to clear input



Button0 = Button(root, text = "0", command = lambda:btnpress(0)) # you can pass in parameter
Button0.grid(row = 4, column = 0)

Button1 = Button(root, text = "1", command = lambda:btnpress(1)) #anonymus functions use lambda keyord
Button1.grid(row = 1, column = 0)

Button2 = Button(root, text = "2", command = lambda:btnpress(2))
Button2.grid(row = 1, column = 1)

Button3 = Button(root, text = "3", command = lambda:btnpress(3))
Button3.grid(row = 1, column = 2)

Button4 = Button(root, text = "4", command = lambda:btnpress(4))
Button4.grid(row = 2, column = 0)

Button5 = Button(root, text = "5", command = lambda:btnpress(5))
Button5.grid(row = 2, column = 1 )

Button6 = Button(root, text = "6", command = lambda:btnpress(6))
Button6.grid(row = 2, column = 2)

Button7 = Button(root, text ="7", command = lambda: btnpress(7))
Button7.grid(row = 3, column = 0)

Button8 = Button(root, text = "8", command = lambda: btnpress(8))
Button8.grid(row = 3, column = 1)

Button9 = Button(root, text = "9", command = lambda: btnpress(9))
Button9.grid(row = 3, column = 2)

Plus = Button(root, text = "+", command = lambda: btnpress("+"))
Plus.grid(row = 1, column = 3)

Subtract = Button(root, text = "-", command = lambda: btnpress("-"))
Subtract.grid(row = 2, column = 3)

Multiply = Button(root, text = "*", command = lambda: btnpress("*"))
Multiply.grid(row = 3, column = 3)

Divide = Button(root, text = "/", command = lambda: btnpress("/"))
Divide.grid(row = 4, column = 3)

Equals = Button(root, text = "=", command = EqualPress)
Equals.grid(row = 4, column = 2)

Clear = Button(root, text = ("C"), command = clear)
Clear.grid(row = 4, column = 1)






root.mainloop()