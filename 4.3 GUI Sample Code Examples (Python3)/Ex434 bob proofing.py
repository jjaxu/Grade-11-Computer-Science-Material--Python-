# Example 4.3.4

from tkinter import*

#BOB PROOFING - Avoid DoubleVar objects as users may type text into them.
#               Use StringVar objects which the user can type anything into them.
#               Then, determine whether StringVar object's value is acceptable
#               or not and convert "Cast" it to a float value if you determine
#               that it is a value number.  This example uses .isdigit() to
#               test the String.
root = Tk()
base = StringVar()
base.set (value = "15")
height = StringVar()
height.set(value = "4")
shape = StringVar()
shape.set(value = "Triangle")
answer = StringVar()
answer.set(value = " ")
                 
def area():
    strBase = base.get()
    strHeight = height.get()
    if strBase.isdigit() and strHeight.isdigit():
        if shape.get() == "Triangle":
            a = 0.5 * float(base.get()) * float(height.get())
        else:
            a = float(base.get()) * float(height.get())
        answer.set ("Area = " + str(a))
    else:
        answer.set ("Incorrect Input")

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
