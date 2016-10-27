#Example 4.3.1

from tkinter import*

master = Tk()
labelString = StringVar("")

def clicked(num):
    labelString.set("Clicked button " + str(num))

button1 = Button (master, text = "Clicked 1",width = 15, height = 3,command = lambda:clicked(1))
button2 = Button (master, text = "Clicked 2",width = 15, height = 3,command = lambda:clicked(2))

button1.pack()
button2.pack()
Label(master,textvariable=labelString,width = 20).pack()
labelString.set("test" )

mainloop()

