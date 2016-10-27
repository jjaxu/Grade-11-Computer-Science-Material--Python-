# Example 4.3.B

from tkinter import *

root = Tk()
root.title ("Events")

c = Canvas(root, width=200, height=200)

def mouseClick(event):
    c.create_oval(event.x,event.y,event.x,event.y,width=1,outline = "black",fill = "black")
    c.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,width=1,outline = "red",fill = "")

    c.update()

def keyPressed (event):
    print ("pressed", event.char)
    c.create_rectangle(event.x-5,event.y-5,event.x+5,event.y+5,width=1,outline = "red",fill = "")
    c.update()

def up(event):
    c.create_line(event.x,event.y,event.x,event.y-100)
    c.update()

c.bind("<Key>", keyPressed)
c.bind("<Button-1>", mouseClick)
c.bind("<Up>",up)
c.pack()
c.focus_set()

mainloop()
