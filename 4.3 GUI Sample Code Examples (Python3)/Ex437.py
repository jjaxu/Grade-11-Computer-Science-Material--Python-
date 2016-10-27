# Example 4.3.7

from tkinter import*

root = Tk()

fnt = IntVar(0)
attr = IntVar(0)
m = StringVar()
m.set (value = "This is the Message")

def display():
    if attr.get() == 0:
        a = "normal"
    elif attr.get() == 1:
        a = "bold"
    else:
        a = "italic"
    if fnt.get() == 0:
        message.config(font=("Times",15,a))
    elif fnt.get() == 1:
        message.config(font=("Arial",15,a))
    else:
        message.config(font=("Vivaldi",15,a))

message = Label(root, textvariable = m,font = ("Times New Roman", 15, "normal"))
message.grid(row = 0, column = 0, columnspan = 2)
fontGroup = LabelFrame(root, text="Font",padx=5, pady=5)
fontGroup.grid(row=1, column = 0)
attrGroup = LabelFrame(root, text="Attribute",padx=5, pady=5)
attrGroup.grid(row=1, column = 1)

Radiobutton (fontGroup,text = "Serif",command = lambda: display(),variable = fnt, value = 0) \
    .grid(row = 0, sticky = W)
Radiobutton (fontGroup, text = "Sans Serif",command = lambda: display(),variable = fnt, value = 1) \
    .grid(row = 1, sticky = W)
Radiobutton (fontGroup, text = "Script",command = lambda: display(),variable = fnt, value = 2) \
    .grid(row = 2, sticky = W)
Radiobutton (attrGroup, text = "Plain",command = lambda: display(),variable = attr,value = 0) \
    .grid(row = 0, sticky = W)
Radiobutton (attrGroup, text = "Bold",command = lambda: display(),variable = attr,value = 1) \
    .grid(row = 1, sticky = W)
Radiobutton (attrGroup, text = "Italic",command = lambda: display(),variable = attr,value = 2) \
    .grid(row = 2, sticky = W)

mainloop()
