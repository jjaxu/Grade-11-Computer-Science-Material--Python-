from tkinter import *

# While Global Variables are not normally used when they can be avoided;
# GUI programming in python requires that they be used on occasion as
# triggering events such as leftMouseClicked and keyPressed do not allow
# the programming to 'add' parameters and pass the reference to the canvas
# into these action procedures.  To provide these action procedures access
# to the canvas and the window 'root' and 'canvas' ID variables, they have
# been declared globally to this code.

root = Tk()
root.title ("My First GUI Window in Python")
canvas = Canvas(root, width = 640, height = 240)

# write all the defs

def keyPressed(event):
    print (event.char)

def leftMouseClicked(event):
    print (event.x, event.y)
    canvas.create_oval(event.x,event.y,event.x+2,event.y+2)


canvas.config(background = "white")
canvas.bind("<Key>",keyPressed)
canvas.bind("<Button-1>", leftMouseClicked)
canvas.pack()
canvas.focus_set()


   
mainloop()
