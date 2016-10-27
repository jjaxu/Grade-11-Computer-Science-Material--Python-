# Example 4.3.5

from tkinter import *

master = Tk()

info = StringVar()
info.set(value = "add this item")

def delete():
    listbox.delete(listbox.index(ACTIVE))

def deleteALL():
    listbox.delete(0,END)

def add ():
    listbox.insert(listbox.index(ACTIVE)+1,info.get())

listbox = Listbox(master)
listbox.pack()

Button (master,text= "Delete Selected",command =lambda: delete()).pack()
Button (master,text= "Delete ALL (Clear)",command =lambda: deleteALL()).pack()
Button (master, text = "Add Text",command =lambda: add()).pack()
Entry (master,width = 20,textvariable = info).pack()
listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()
