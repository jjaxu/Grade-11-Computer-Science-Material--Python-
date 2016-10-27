# Example 4.3.9

from tkinter import*

master = Tk()
scroll = Scrollbar (master)
scroll.pack(side = RIGHT,fill = Y)

listbox = Listbox(master,yscrollcommand = scroll.set)

for i in range(100):
    listbox.insert(END, str(i))

listbox.pack(side=LEFT, fill=BOTH)
scroll.config(command=listbox.yview)

mainloop()
