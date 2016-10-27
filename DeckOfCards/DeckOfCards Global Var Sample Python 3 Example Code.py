import random
from tkinter import*

table = Tk()
canvas=Canvas(table,width=200,height=200)
canvas.place(x = 60, y = 20)

def deal():

    global picture
    # The PhotoImage variable picture must remain referenced and available
    # to the canvas to know where the photo reference is; hence it has
    # been made global so that the canvas always knows of the last card
    # displayed.
    
    face = random.randint(1,13)
    s = random.randint(1,4)
    if s == 1:
       suit = "h"
    elif s == 2:
       suit = "c"
    elif s == 3:
       suit = "d"
    else:
       suit = "s"
       
    if face == 1:
       n = "a" 
    elif face == 10:
       n = "t" 
    elif face == 11:
       n = "j" 
    elif face == 12:
       n = "q" 
    elif face == 13:
       n = "k"
    else:
       n = str(face)

    picture = PhotoImage (file = n + str(suit) + ".gif")
    canvas.create_image(5,5,image=picture,anchor=NW)
    
    # print (n + str(suit))
    
#============================
#MAIN

deald = Button (table, text ="Random Card", command = lambda:deal())
deald.place(x = 60, y = 170)

table.mainloop()
