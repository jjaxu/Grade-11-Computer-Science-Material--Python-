from tkinter import *

n = 100



root = Tk()
root.title("Etch-a-Sketch")
canvas = Canvas(None, width = 500, height = 400)
canvas.pack()

while n != 200:
    #canvas.create_line(x1, y1, x2, y2, fill = "Colour",width = thickness)
    canvas.create_line(300,400,100,200,fill = "Red",width = n)
    #canvas.create_line(0,,400,100,fill = "blue")
    

    n = n + 1

mainloop()
