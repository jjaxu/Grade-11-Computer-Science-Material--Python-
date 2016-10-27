# Example 4.3.8

from tkinter import*

root = Tk()
def out():
    print (widget.get())

widget = Scale (root, from_ = 10, to = 100,resolution = 0.1,orient = HORIZONTAL)
widget.pack()
widget.set(50)

button = Button (root, text = "Print",command = lambda: out())
button.pack()

mainloop()
