#Example 4.3.2 (D)
#printing text to an existing canvas that was created 'globally' to avoid
#excessive parameter passing; as the canvas name 'c' would have to be passed
#from the MAIN as a parameter into the function displaySample() for this
#function to see and print to the canvas... so an exception was made, making
#the canvas and the window global so that all functions can see and use
#these GUI widgets

from tkinter import *

root = Tk()
c = Canvas (root, width = 400, height = 200)
c.pack()
c.config (background = "peach puff")

def displaySample():    
    for i in range(0,5):
        for j in range(0,i):
            c.create_text(25*j,25*i,anchor=SW,text = "*",font = ("Arial", "14", "bold italic"))


displaySample()
# no user input; so no mainloop() really required.
# mainloop()
