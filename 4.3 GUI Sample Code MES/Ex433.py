# Example 4.3.3

from tkinter import*
root = Tk()

days = StringVar("")

def select():
    days.set("Selected: " + v1.get() + " " + v2.get() + " " + v3.get())

lbl1 = Label (root,
text = "Which day can you work?")
lbl1.grid(row=0, sticky=W, padx = 10, pady = 5)
v1 = StringVar()
v1.set(value = " ")
v2 = StringVar()
v2.set(value = " ")
v3 = StringVar()
v3.set(value = " ")
frame = Frame(root, relief=GROOVE, borderwidth = 3)
frame.grid(row=1, sticky=W, padx = 10, pady = 5)
checkbtn1 = Checkbutton(frame, text = "Monday",variable = v1, onvalue = "Monday",offvalue = " ")
checkbtn2 = Checkbutton(frame, text = "Tuesday",variable = v2, onvalue = "Tuesday",offvalue = " ")
checkbtn3 = Checkbutton(frame, text="Wednesday",variable = v3, onvalue = "Wednesday",offvalue = " ")
checkbtn1.grid(row=0, sticky=W, padx = 5)
checkbtn2.grid(row=1, sticky=W, padx = 5)
checkbtn3.grid(row=2, sticky=W, padx = 5)
buttonSelect = Button (root, text = "Select",width = 20, height = 2,command = lambda:select())
buttonSelect.grid(row=2, sticky=W,padx = 10, pady = 5)
lbl2 = Label (root, textvariable = days, width = 30,anchor = W, font = ("Arial", "12", "bold"))
lbl2.grid(row=3, sticky=W, padx = 10, pady = 5)

mainloop()
