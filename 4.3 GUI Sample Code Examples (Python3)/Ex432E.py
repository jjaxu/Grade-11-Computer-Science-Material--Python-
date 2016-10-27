# Example 4.3.2 (E)
# At the request of a student; demonstrating the idea behind scaling an drawn
# object.

from tkinter import *
import random

class Dice:
    def __init__(self, size = 100):
        self.value = random.randint(1,6)
        self.size = size
        self.radius = self.size / 5
        self.gap = self.radius / 2
        
    def draw (self, c, x, y):
        c.create_rectangle(x, y, x + self.size, y + self.size,
                           width = 3, fill = "ivory")       

    def setSize (self,size=100):
        # This has not be 'bob' or boundary proofed in this example.
        self.size = size
        # While radius and gap are referenced here and changed; not actually used in
        # this example's output
        self.radius = self.size / 5
        self.gap = self.radius / 2
  
def keyPressed (event):
    global canvas
    if event.char == "h":
        #instruct object mySquare to set itself to size 80
        mySquare = Dice(size=80)
        mySquare.draw(canvas, 20, 60)

        #instruct object mySquare to set itself to size 80
        mySquare.setSize(40)
        mySquare.draw(canvas, 150, 60)

        #instruct object mySquare to set itself to size 80
        mySquare.setSize(40)
        mySquare.draw(canvas, 280, 60)

        #this 'refreshes' the canvas as sometime draws don't show directly.
        canvas.update()
        
    elif event.char == "g":
        print
        # simulation loop/logic here
    else:
        root.destroy()
    

root = Tk()
root.title ("A Demo of sizing an graphic object on a canvas")

canvas = Canvas(root, width = 400, height = 200)
canvas.config(background = "white")
canvas.create_text(10,40,anchor=SW,text = "Press h to draw; anything else to quit", font=("Arial","14","bold"))
canvas.bind("<Key>", keyPressed)
canvas.pack()
canvas.focus_set()

mainloop()
