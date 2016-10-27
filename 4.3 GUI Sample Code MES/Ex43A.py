# Example 4.3.A

from tkinter import*

root = Tk()

textbox = Text (root, height = 10, width = 30)

textbox.grid(row = 0, column = 0, columnspan = 3)

def dump():
    print (textbox.get (1.0, END))
    textbox.insert(INSERT, "Hi\n")
    textbox.insert(INSERT, "I'm Back\n")
    textbox.insert(INSERT, "Doc?")

def clear():
    textbox.delete(1.0,END)

textbox.insert(INSERT, "Hi\n")
textbox.insert(INSERT, "What's up\n")
textbox.insert(INSERT, "Doc?")

##-----------------------------------

dumpButton = Button (root, text = "Dump",width = 10, height = 2,command = lambda:dump())
dumpButton.grid(row = 1,column = 0)
clearButton = Button (root, text = "Clear",width = 10, height = 2,command =  lambda:clear())
clearButton.grid(row = 1,column = 1)
exitButton = Button (root, text = "Exit",width = 10, height = 2,command = lambda: root.destroy())
exitButton.grid(row = 1,column = 2)



##
##--------------------------------------
##
mainloop()
print("done")
