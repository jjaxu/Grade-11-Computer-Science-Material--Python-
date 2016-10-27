import random
from tkinter import*

#============================
#MAIN
table = Tk()
canvas=Canvas(table,width=300,height=300)
canvas.pack()
picture = PhotoImage (file="2c.gif")
canvas.create_image(5,5,image=picture,anchor=NW)
