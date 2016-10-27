#Example 4.3.2 (C)

from tkinter import *

c = Canvas (None, width = 400, height = 200)
c.pack()

c.config (background = "peach puff")

# c.create_line (0,100,400,100,fill = "red")

#for i in range(1,4):
#    c.create_line (100*i,0,100*i,400,fill = "RoyalBlue1")
    
for i in range(0,5):
    for j in range(0,i):
        c.create_text(25*j,25*i,anchor=SW,text = "*",font = ("Arial", "14", "bold italic"))

mainloop()
