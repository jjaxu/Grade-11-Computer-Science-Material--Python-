#Example 4.3.2 (A)

from tkinter import *

c = Canvas (None, width = 400, height = 200)
c.pack()

c.config (background = "peach puff")
c.create_line (0,100,400,100,fill = "red")

for i in range(1,4):
    c.create_line (100*i,0,100*i,400,fill = "RoyalBlue1")
    
c.create_arc (20,20,80,80,start = 45,extent = 270, outline = "black",fill = "white", style = PIESLICE)
c.create_arc (120,20,180,80,start = 45,extent = 90, outline = "black",width = 3.5, style = CHORD)
c.create_arc (220,20,280,80,start = 315,extent = -90, outline = "blue",width = 2.0, style = ARC)
c.create_text(320,70,anchor=SW,text = "Arcs",font = ("Arial", "24", "bold italic"))
c.create_rectangle(20,120,80,180,width=2.5,outline="green", fill="red")
c.create_oval(120,120,180,180,width=1.5,outline="black", fill = "")
c.create_polygon(230,120,270,120,290,150,270,180,230,180,210,150,width = 5, outline = "purple")

mainloop()
