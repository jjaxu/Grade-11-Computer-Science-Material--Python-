# Example 4.3.C

from tkinter import *

from tkinter import messagebox

top = Tk()
def showinfo():
    messagebox.showinfo("Say Hello","Hello World.")

def showwarning():
    messagebox.showwarning("Warning","You may have a virus!")

def showerror():
    messagebox.showerror("Error","You Do have a virus!")

def showquestion():
    x = messagebox.askquestion ("Question","Do you have a virus?")
    print (x)

def showokcancel():
    x = messagebox.askokcancel("ok cancel","Ok to delete?")
    print (x)

def showyesno():
    x = messagebox.askyesno("Yes No","Do you WANT a virus?")
    print (x)

def showretrycancel():
    x = messagebox.askretrycancel("Retry Cancel","Virus not deleted.")
    print (x)

Button(top, text = "Info",command = showinfo).pack()
Button(top, text = "Warning",command = showwarning).pack()
Button(top, text = "Error",command = showerror).pack()
Button(top, text = "Question",command = showquestion).pack()
Button(top, text = "ok Cancel",command = showokcancel).pack()
Button(top, text = "Yes No",command = showyesno).pack()
Button(top, text = "Retry Cancel",command = showretrycancel).pack()

top.mainloop()
