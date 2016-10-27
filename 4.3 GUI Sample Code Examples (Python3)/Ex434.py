# Example 4.3.4

from tkinter import*

root = Tk()

base = DoubleVar(0)
base.set (value = 15.17)
height = DoubleVar()
height.set(value = 4.3)
shape = StringVar()
shape.set(value = "triangle")
answer = StringVar()
answer.set(value = " ")
                 
def area():
    if shape.get() == "triangle":
        a = 0.5 * float(base.get()) * float(height.get())
    else:
        a = float(base.get()) * float(height.get())
    answer.set ("Area = " + str(a))

Label (root, text="Base:").grid(row=0,column=0, sticky=W, padx = 10, pady = 5)
Label (root, text="Height:").grid(row=1,column=0, sticky=W,padx = 10, pady = 5)
Label (root, text="Shape:").grid(row=2,column=0, sticky=W,padx = 10, pady = 5)

Entry (root, width = 8, textvariable = base). \
    grid (row= 0 , column = 1, padx = 10, pady = 5)
Entry (root, width = 8, textvariable = height). \
    grid (row= 1 , column = 1, padx = 10, pady = 5)
Entry (root, width = 8, textvariable = shape). \
    grid (row= 2 , column = 1, padx = 10, pady = 5)

Button (root, text = "Calculate Area", width = 18,height = 2,command = lambda:area()).grid (row= 3,column = 0, columnspan = 2, padx = 10, pady = 5)

Label (root, textvariable = answer,width = 15, height = 2,font=("Arial","12","bold")).grid(row=4,column=0, columnspan = 2, sticky=W,padx = 10, pady = 5)

mainloop()

