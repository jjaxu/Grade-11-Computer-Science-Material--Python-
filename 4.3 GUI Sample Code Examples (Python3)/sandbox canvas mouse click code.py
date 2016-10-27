from tkinter import *

# write all the defs

def keyPressed(event):
    print (event.char)

def leftMouseClicked(event):
    print (event.x, event.y)

root = Tk()
root.title ("My First GUI Window in Python")


canvas = Canvas(root, width = 640, height = 240)
canvas.config(background = "white")
canvas.bind("<Key>",keyPressed)
canvas.bind("<Button-1>", leftMouseClicked)
canvas.pack()
canvas.focus_set()

# all the calls necessary to draw something interesting
   
mainloop()
