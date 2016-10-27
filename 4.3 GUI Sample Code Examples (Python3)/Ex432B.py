#Example 4.3.2 (B)

import time
from tkinter import *

c = Canvas (None, width = 410, height = 60)
c.pack()
c.config (background = "white")
c.create_rectangle(5,5,405,55,width=2.0,outline="black", fill="")
bar = c.create_rectangle(10,10,10,50,width=0,fill="grey")

for x in range(10,401):
    c.coords(bar, 10,10,x,50)
    c.update()
    time.sleep(0.01)

c.delete(ALL)
c.create_text(205,30,anchor = CENTER,text = "Completed!",font=("Comic Sans MS","20","bold"))

mainloop()
