# Author: Jackie Xu
# Date: 1/6/2015
# Purpose: Creating myList1 compostion of classes with myList1 List
#======================================================
import random
from tkinter import *

root = Tk(className = " 1D lists in Python")
root.config(width = 1200, height = 700)

#-------------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/6/2014
# Purpose: "Bob" check function
# Parameters: String input
# Return Value: True/False

def bobRangeCheck(strInput,low = "NA",high = "NA"):
    ok = False
    
    if strInput.isdigit():
        if low == "NA" and high == "NA":
            ok = True
        elif low == "NA":
            if int(strInput) <= high:
                ok = True
        elif high == "NA":
            if int(strInput) >= low:
                ok = True
        else:
            if int(strInput) >= low and int(strInput) <= high:
                ok = True
    return ok

class IntGroup:

# Author: Jackie Xu
# Date: 1/6/2015
# Purpose: Class with myList1 list as one of its data fields
# Data fields ----------
#   list: the list of the object
#   size: size of the list of the object
# Methods---------------
#   initAsNum: Creates list with value in the Parameters
#   initAsSequence: Creates list with values, 1,2,3,4... given its size
#   initAsFib: Creates list with values of myList1 Fibonacci sequence, given its size
#   calcTotal: Calculates the sum of all elements in the list
#   calcMean: Calculates the mean of all elements in the list
#   findLargest: Returns the value of the largest element in the list
#   calcFreq: Returns the number of elements in the list that matches the Parameters value
#   insertAt: Inserts an element in the list given its index and value
#   removeAt: Removes an element in the list given its index and value
#   removeAll: Removes all elements in the list that matches the Parameters value
#   findFirst: Returns the index of the first element that matches the Parameters value
#   reverse: Reverses the order of the elements in the list
#   isSorted: Checks if the the list is in acending order
#   merge: adds itself to another list then sorts itself in acending order
#   __str__: Converts object into myList1 string which contains its list and its size
#   __eq__: Overloaded operator that checks if itself is equal to another intGroup object
#   __lt__: Overloaded operator that checks if itself is less than another intGroup object
#   __le__: Overloaded operator that checks if itself is less or equal to another intGroup object
#   __gt__: Overloaded operator that checks if itself is greater than another intGroup object
#   __ge__: Overloaded operator that checks if itself is greater or equal to another intGroup object
#   __ne__: Overloaded operator that checks if itself is NOT equal to another intGroup object
#   __add__: Overloaded operator that adds the list of another intGroup oject to itself, but does not sort it

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/6/2015
    # Purpose: Constructor for tbe IntGroup Class
    # Parameters: self, size
    # Return: -


    def __init__(self,size = 0):
        self.size = size
        self.list = []

        for count in range(1,size + 1):
            randNum = random.randint(0,size)
            self.list.append(randNum)

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/6/2015
    # Purpose: Converts object to myList1 string
    # Parameters: self
    # Return: self as myList1 string
    
    def __str__(self):
        return str(self.list) + "[Size: " + str(self.size) + "]"

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/6/2015
    # Purpose: Creates myList1 list with given size, with elements of the size
    # Parameters: self, size
    # Return: -
    
    def initAsNum(self,listSize = 0):
        self.list = []
        self.size = listSize
        for count in range(1,listSize + 1):
            self.list.append(listSize)
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/6/2015
    # Purpose: Creates myList1 list of myList1 sequrnce 1,2,3,4...until its given size
    # Parameters: self, size
    # Return: -
    
    def initAsSequence(self,listSize = 0):
        self.list = []
        self.size = listSize
        for count in range(1,listSize + 1):
            self.list.append(count)

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/7/2015
    # Purpose: Creates myList1 list of myList1 Fibinacci sequence
    # Parameters: self, size
    # Return: -

    def initAsFib(self,listSize = 0):
        self.list = []
        self.size = listSize
        
        current = 0
        prev = 1
        next = current + prev

        
        for count in range(1,listSize + 1):
            self.list.append(next)

            prev = current
            current = next
            next = prev + current
            
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/7/2015
    # Purpose: Returns the sum of all the elements in the list
    # Parameters: self
    # Return: sum

    def calcTotal(self):
        sum = 0
        for count in range(0,self.size):
            sum = sum + self.list[count]
        return sum

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/7/2015
    # Purpose: Returns the average of all the elements in the list 
    # Parameters: self
    # Return: mean

    def calcMean(self):
        mean = 0
        if self.size != 0:
            mean = self.calcTotal() / self.size
        return mean

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/7/2015
    # Purpose: Returns the largest element in the list
    # Parameters: self
    # Return: largest

    def findLargest(self):
        largest = -1
        for count in range(0,self.size):
            if self.list[count] > largest:
                largest = self.list[count]
        if largest == -1:
            largest = "No largest value, this list is empty"
        return largest

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/7/2015
    # Purpose: Returns count of the an element given in myList1 Parameters
    # Parameters: self, value
    # Return: amount

    def calcFreq(self,value = 0):
        amount = 0
        for count in range(0,self.size):
            if self.list[count] == value:
                amount = amount + 1
        return amount

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Inserts myList1 value in myList1 desinated position in the list
    # Parameters: self, postition, value
    # Return: -

    def insertAt(self, position = 0, value = 0):
        if position >= 0 and position <= self.size:
            self.list.insert(position,value)
            self.size = self.size + 1
        else:
            print("Cannot insert, partition does not exist")

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Removes myList1 value in myList1 desinated position in the list
    # Parameters: self, postition
    # Return: -

    def removeAt(self, position = 0):
        if position >= 0 and position <= self.size - 1:
            del self.list[position]
            self.size = self.size - 1
        else:
            print("Cannot remove, partition does not exist")

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Removes all values in the list that matches the Parameters
    # Parameters: self, value
    # Return: -

    def removeAll(self, value = 0):
        amount = self.calcFreq(value)
        for count in range(0,amount):
           self.list.remove(value)
           self.size = self.size - 1

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Returns location of the first element in the Parameters
    # Parameters: self, value
    # Return: -

    def findFirst(self,value):
        count = 0
        if self.list.count(value) != 0:
            while self.list[count] != value :
                count = count + 1
        else:
            count = -1
        return count
                

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Reverses the list
    # Parameters: self
    # Return: new (reversed list)

    def reverse(self):   
        for count in range(0,self.size):
            self.list.append(self.list.pop(self.size - count - 1))


    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Checks if the list is sorted in acending order
    # Parameters: self
    # Return: -

    def isSorted(self):
        sorted = False
        yes = 0
        
        if self.size == 0:
            yes = -1
        else:
            for count in range(0,self.size - 1):
                if self.list[count] <= self.list[count + 1]:
                    yes = yes + 1
    
        if yes == self.size - 1:
            sorted = True
        return sorted

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/8/2015
    # Purpose: Merges two sorted lists
    # Parameters: self, secondIntGroup
    # Return: merged

    def merge(self,secondIntGroup):
        merged = IntGroup()
        
        for count in range(0,self.size):
            merged.insertAt(0,self.list[count])
            merged.list.sort()

        for count in range(0,secondIntGroup.size):
            merged.insertAt(0,secondIntGroup.list[count])
            merged.list.sort()

        return merged

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself and given list is exactly the same
    # Parameters: self, secondIntGroup
    # Return: True/False

    def __eq__(self,secondIntGroup):
        equal = False
        if self.list == secondIntGroup.list:
            equal = True
        return equal

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself is less than myList1 given list
    # Parameters: self, secondIntGroup
    # Return: True/False

    def __lt__(self,secondIntGroup):
        less = False
        if self.list < secondIntGroup.list:
            less = True
        return less
    
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself is less or equal to myList1 given list
    # Parameters: self, secondIntGroup
    # Return: True/False
       
    def __le__(self,secondIntGroup):
        lessEqual = False
        if self.list <= secondIntGroup.list:
            lessEqual = True
        return lessEqual

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself is greater than myList1 given list
    # Parameters: self, secondIntGroup
    # Return: True/False

    def __gt__(self,secondIntGroup):
        greater = False
        if self.list > secondIntGroup.list:
            greater = True
        return greater

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself is greater or equal to myList1 given list
    # Parameters: self, secondIntGroup
    # Return: True/False

    def __ge__(self,secondIntGroup):
        greaterEqual = False
        if self.list >= secondIntGroup.list:
            greaterEqual = True
        return greaterEqual
    
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: checks whether itself and given list is NOT the same
    # Parameters: self, secondIntGroup
    # Return: True/False

    def __ne__(self,secondIntGroup):
        notEqual = False
        if self.list != secondIntGroup.list:
            notEqual = True
        return notEqual

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/9/2015
    # Purpose: Adds two intGroups together, but will not sort
    # Parameters: self, secondIntGroup
    # Return: newIntGroup

    def __add__(self,secondIntGroup):
        newIntGroup = IntGroup()
        newIntGroup.list = self.list + secondIntGroup.list
        newIntGroup.size = self.size + secondIntGroup.size
        return newIntGroup



optList1 = IntVar()
optList1.set(value=0)
optList2 = IntVar()
optList2.set(value=0)

#------------------------------------------------------
# Author: Jackie Xu
# Date: 1/12/2015
# Purpose: This function will adjust the values of the option boxes
# Parameters: -
# Return: -

def options():
    global list1
    global list2
    
    if optList1.get() == 0:
        list1 = "num"
    elif optList1.get() == 1:
        list1 = "seq"
    elif optList1.get() == 2:
        list1 = "fib"
        
    if optList2.get() == 0:
        list2 = "num"
    elif optList2.get() == 1:
        list2 = "seq"
    elif optList2.get() == 2:
        list2 = "fib"

#------------------------------------------------------
# Author: Jackie Xu
# Date: 1/12/2015
# Purpose: This is the "Master" function for the GUI
# Parameters: first, second
# Return: -

def go(initial = False):

    window.create_rectangle(0,100,1200,700, fill = "bisque2", outline = "bisque2")
    window.create_text(460, 130, anchor = W, text = "List 1", font = ("Calibri","16","bold"))
    window.create_text(460, 300, anchor = W, text = "List 2", font = ("Calibri","16","bold"))

    good1 = False
    good2 = False


    if bobRangeCheck(txtBox1.get(),0,20):
        good1 = True
        if initial:
            if list1 == "num":
                myList1.initAsNum(int(txtBox1.get()))

            elif list1 == "seq":
                myList1.initAsSequence(int(txtBox1.get()))
                
            elif list1 == "fib":
                myList1.initAsFib(int(txtBox1.get()))
            
           
        lblOut1.config(text = myList1,wraplength = 300)
        lblOut1.place(x = 460, y = 150)

    else:
        lblOut1.place_forget()
        window.create_text(500, 200, anchor = W, text = "Invalid Input!", font = ("Calibri","16"))




    if bobRangeCheck(txtBox2.get(),0,20):
        good2 = True
        if initial:
            if list2 == "num":
                myList2.initAsNum(int(txtBox2.get()))
            elif list2 == "seq":
                myList2.initAsSequence(int(txtBox2.get()))
            elif list2 == "fib":
                myList2.initAsFib(int(txtBox2.get()))

        lblOut2.config(text = myList2,wraplength = 300)
        lblOut2.place(x = 460, y = 320)

    else:
        lblOut2.place_forget()
        window.create_text(500, 400, anchor = W, text = "Invalid Input!", font = ("Calibri","16"))
        

    if good1 and good2:
        window.create_text(25, 500, anchor = W, text = "List 1 Modifications", font = ("Calibri","16","bold"))
        window.create_text(250, 500, anchor = W, text = "List 2 Modifications", font = ("Calibri","16","bold"))
        
        txtMod1.place(x = 25,y = 520)
        txtMod2.place(x = 250,y = 520)

        cmdCalcFreq1.place(x = 25, y = 550)
        cmdFindFirst1.place(x = 25, y = 600)
        cmdRemoveAll1.place(x = 25, y = 650)
        
        cmdInsert1.place(x = 125, y = 600)
        cmdRemove1.place(x = 125, y = 650)
        cmdReverse1.place(x = 125, y = 550)
        

        cmdCalcFreq2.place(x = 250, y = 550)
        cmdFindFirst2.place(x = 250, y = 600)
        cmdRemoveAll2.place(x = 250, y = 650)
        
        cmdInsert2.place(x = 350, y = 600)
        cmdRemove2.place(x = 350, y = 650)
        cmdReverse2.place(x = 350, y = 550)
        

        window.create_text(780, 160, anchor = W, text = "Sum of elements in list 1: " + str(myList1.calcTotal()), font = ("Calibri","16","bold","underline"))
        window.create_text(780, 180, anchor = W, text = "Average of elements in list 1: " + str(round(myList1.calcMean(),2)), font = ("Calibri","16","bold","underline"))
        window.create_text(780, 200, anchor = W, text = "Is list 1 sorted? : " + str(myList1.isSorted()), font = ("Calibri","16","bold","underline")) 
        window.create_text(780, 220, anchor = W, text = "Largest value: " + str(myList1.findLargest()), font = ("Calibri","16","bold","underline"))

        window.create_text(780, 300, anchor = W, text = "Sum of elements in list 2: " + str(myList2.calcTotal()), font = ("Calibri","16","bold","underline"))
        window.create_text(780, 320, anchor = W, text = "Average of elements in list 2: " + str(round(myList2.calcMean(),2)), font = ("Calibri","16","bold","underline"))
        window.create_text(780, 340, anchor = W, text = "Is list 2 sorted? : " + str(myList2.isSorted()), font = ("Calibri","16","bold","underline")) 
        window.create_text(780, 360, anchor = W, text = "Largest value: " + str(myList2.findLargest()), font = ("Calibri","16","bold","underline"))
        
        lblMerge.config(text = "Merged List: " + str(myList1.merge(myList2)),wraplength = 500)
        lblMerge.place(x = 460, y = 400)

        lblConcat.config(text = "Concatenated List: " + str(myList1 + myList2),wraplength = 500)
        lblConcat.place(x = 460, y = 500)
        
        window.create_text(460, 610, anchor = W, text = "List 1 is equal to list 2: " + str(myList1 == myList2), font = ("Calibri","14"))
        window.create_text(460, 640, anchor = W, text = "List 1 is less or equal to list 2: " + str(myList1 <= myList2), font = ("Calibri","14"))
        window.create_text(460, 670, anchor = W, text = "List 1 is less than list 2: " + str(myList1 < myList2), font = ("Calibri","14"))
        
        window.create_text(800, 610, anchor = W, text = "List 1 is greater or equal to list 2: " + str(myList1 >= myList2), font = ("Calibri","14"))
        window.create_text(800, 640, anchor = W, text = "List 1 is greater than list 2: " + str(myList1 > myList2), font = ("Calibri","14"))
        window.create_text(800, 670, anchor = W, text = "List 1 is NOT equal to list 2: " + str(myList1 != myList2), font = ("Calibri","14"))

    else:
        
        cmdCalcFreq1.place_forget()
        cmdFindFirst1.place_forget()
        cmdRemoveAll1.place_forget()
        
        cmdInsert1.place_forget()
        cmdRemove1.place_forget()
        

        cmdCalcFreq2.place_forget()
        cmdFindFirst2.place_forget()
        cmdRemoveAll2.place_forget()
        
        cmdInsert2.place_forget()
        cmdRemove2.place_forget()

        txtMod1.place_forget()
        txtMod2.place_forget()

        cmdReverse1.place_forget()
        cmdReverse2.place_forget()
        lblMerge.place_forget()
        lblConcat.place_forget()

#------------------------------------------------------
# Author: Jackie Xu
# Date: 1/15/2015
# Purpose: A small function that checks the insertAt and removeAt syntax
# Parameters: text
# Return: ok 

def insertRemoveCheck(text):
    ok = False
    if "," in text:
        ok = True
    return ok
            

#------------------------------------------------------
# Author: Jackie Xu
# Date: 1/15/2015
# Purpose: Function that takes care of list modifications done to list 1
# Parameters: function, value
# Return: -

def mod1(function, value):
    window.create_rectangle(780,240,1200,280, fill = "bisque2", outline = "bisque2")
    if function == "reverse1":
        myList1.reverse()
        go()
    elif bobRangeCheck(value,0,"NA"):
        value = int(value)
        if function == "freq1":
            myList1.calcFreq(value)
            window.create_text(780, 260, anchor = W, text = "Number of " + str(value) + "s: " + str(myList1.calcFreq(value)), font = ("Calibri","14","bold"))
        elif function == "findFirst1":
            myList1.findFirst(value)
            window.create_text(780, 260, anchor = W, text = "Index of first " + str(value) + ": " + str(myList1.findFirst(value)), font = ("Calibri","14","bold"))
        elif function == "removeAll1":
            myList1.removeAll(value)
            go()
        elif function == "remove1":
            myList1.removeAt(value)
            go()
            
    elif function == "insert1":
        pos = "-1"
        val = "-1"
        
        if insertRemoveCheck(txtMod1.get()):
            posVal = txtMod1.get().strip().split(",")
            pos = posVal[0]
            val = posVal[1]
        
        if bobRangeCheck(pos,0,myList1.size) and bobRangeCheck(val,"NA","NA") and myList1.size < 20:
            pos = int(pos)
            val = int(val)
            myList1.insertAt(pos,val)
            go()
        else:
            print("Cannot insert, bad inputs or max size exceeded(20)!")
    else:
        go()
        print("Error, inputs not numbers!")

#------------------------------------------------------
# Author: Jackie Xu
# Date: 1/16/2015
# Purpose: Function that takes care of list modifications done to list 2
# Parameters: function, value
# Return: -

def mod2(function, value):
    window.create_rectangle(780,370,1200,460, fill = "bisque2", outline = "bisque2")
    if function == "reverse2":
        myList2.reverse()
        go()
    elif bobRangeCheck(value,0,"NA"):
        value = int(value)
        if function == "freq2":
            myList2.calcFreq(value)
            window.create_text(780, 380, anchor = W, text = "Number of " + str(value) + "s: " + str(myList2.calcFreq(value)), font = ("Calibri","14","bold"))
        elif function == "findFirst2":
            myList2.findFirst(value)
            window.create_text(780, 380, anchor = W, text = "Index of first " + str(value) + ": " + str(myList2.findFirst(value)), font = ("Calibri","14","bold"))
        elif function == "removeAll2":
            myList2.removeAll(value)
            go()
        elif function == "remove2":
            myList2.removeAt(value)
            go()
            
    elif function == "insert2":
        pos = "-1"
        val = "-1"
        
        if insertRemoveCheck(txtMod2.get()):
            posVal = txtMod2.get().strip().split(",")
            pos = posVal[0]
            val = posVal[1]
        
        if bobRangeCheck(pos,0,myList2.size) and bobRangeCheck(val,"NA","NA") and myList2.size < 20:
            pos = int(pos)
            val = int(val)
            myList2.insertAt(pos,val)
            go()
        else:
            print("Cannot insert, bad inputs or max size exceeded(20)!")
    else:
        go()
        print("Error, inputs not numbers!")
        
#MAIN================
print('''Help:
 - When using 'insert', the syntax for the text box is 'index,value'.
 - Max list size is 20, don't go beyond 20.
 - lists only support integer inputs, not floats or strings.''')

myList1 = IntGroup()
myList2 = IntGroup()

input1 = StringVar()
input2 = StringVar()

objMod1 = StringVar()
objMod2 = StringVar()

input1.set(value = "10")
input2.set(value = "10")

objMod1.set(value = "")
objMod2.set(value = "")

#Main canvas
window = Canvas(root,width = 1200, height = 700,bg = "bisque2")
window.place(x = 0,y = 0)

window.create_text(25, 50, anchor = W, text = "1D lists in Python", font = ("Calibri","36","bold"))

#List Frames
listGroup1 = LabelFrame(window, text = "List 1",font = ("Calibri","30","bold","underline"),height = 300, width = 200,bg = "bisque2")
listGroup1.place(x = 25, y = 100)

listGroup2 = LabelFrame(window, text = "List 2",font = ("Calibri","30","bold","underline"),height = 300, width = 200,bg = "bisque2")
listGroup2.place(x = 250, y = 100)

#option buttons
optNum1 = Radiobutton(listGroup1, text = "List of same numbers",value = 0, variable = optList1, bg = "bisque2", font = ("Calibri","14"), command = lambda:options())
optNum2 = Radiobutton(listGroup2, text = "List of same numbers",value = 0, variable = optList2, bg = "bisque2", font = ("Calibri","14"), command = lambda:options())

optSequence1 = Radiobutton(listGroup1, text = "List of a Sequence", value = 1, variable = optList1, bg = "bisque2", font = ("Calibri","14"), command = lambda:options())
optSequence2 = Radiobutton(listGroup2, text = "List of a Sequence", value = 1, variable = optList2, bg = "bisque2", font = ("Calibri","14"), command = lambda:options())

optFib1 = Radiobutton(listGroup1, text = "List of a Fibonacci Sequence", value = 2, variable = optList1, bg = "bisque2", font = ("Calibri","14"), wraplength=150, justify=LEFT, command = lambda:options())
optFib2 = Radiobutton(listGroup2, text = "List of a Fibonacci Sequence", value = 2, variable = optList2, bg = "bisque2", font = ("Calibri","14"), wraplength=150, justify=LEFT,command = lambda:options()) 

optNum1.place(x = 0, y = 0)
optNum2.place(x = 0, y = 0)

optSequence1.place(x = 0, y = 50)
optSequence2.place(x = 0, y = 50)

optFib1.place(x = 0, y = 100)
optFib2.place(x = 0, y = 100)

#List size editor
lblList1 = Label(listGroup1, text = "Size of List 1:", bg = "bisque2", font = ("Calibri","14","bold"))
lblList1.place(x = 10, y = 160)

lblList2 = Label(listGroup2, text = "Size of List 2:", bg = "bisque2", font = ("Calibri","14","bold"))
lblList2.place(x = 10, y = 160)

txtBox1 = Entry(listGroup1,textvariable = input1,width = 20, font = ("Calibri","12"))
txtBox2 = Entry(listGroup2,textvariable = input2,width = 20, font = ("Calibri","12"))

txtBox1.place(x = 10, y = 200)
txtBox2.place(x = 10, y = 200)

#Output labels
lblOut1 = Label(window, bg = "bisque2",font = ("Calibri","14"))
lblOut2 = Label(window, bg = "bisque2", font = ("Calibri","14"))
lblMerge = Label(window, bg = "bisque2", font = ("Calibri","14"))
lblConcat = Label(window, bg = "bisque2", font = ("Calibri","14"))

#List modification
txtMod1 = Entry(window,textvariable = objMod1,width = 20, font = ("Calibri","12"))
txtMod2 = Entry(window,textvariable = objMod2,width = 20, font = ("Calibri","12"))

cmdCalcFreq1 = Button(window,text = "Frequency", font = ("Calibri","12"), command = lambda:mod1("freq1", txtMod1.get()))
cmdFindFirst1 = Button(window,text = "Find First", font = ("Calibri","12"), command = lambda:mod1("findFirst1", txtMod1.get()))
cmdInsert1 = Button(window,text = "Insert", font = ("Calibri","12"), command = lambda:mod1("insert1", txtMod1.get()))
cmdRemove1 = Button(window,text = "Remove", font = ("Calibri","12"), command = lambda: mod1("remove1", txtMod1.get()))
cmdRemoveAll1 = Button(window,text = "Remove All", font = ("Calibri","12"), command = lambda:mod1("removeAll1",txtMod1.get()))
cmdReverse1 = Button(window,text = "Reverse", font = ("Calibri","12"), command = lambda:mod1("reverse1",txtMod1.get()))


cmdCalcFreq2= Button(window,text = "Frequency", font = ("Calibri","12"), command = lambda:mod2("freq2", txtMod2.get()))
cmdFindFirst2 = Button(window,text = "Find First", font = ("Calibri","12"), command = lambda:mod2("findFirst2", txtMod2.get()))
cmdInsert2 = Button(window,text = "Insert", font = ("Calibri","12"), command = lambda:mod2("insert2", txtMod2.get()))
cmdRemove2 = Button(window,text = "Remove", font = ("Calibri","12"), command = lambda: mod2("remove2", txtMod2.get()))
cmdRemoveAll2 = Button(window,text = "Remove All", font = ("Calibri","12"), command = lambda:mod2("removeAll2",txtMod2.get()))
cmdReverse2 = Button(window,text = "Reverse", font = ("Calibri","12"), command = lambda:mod2("reverse2",txtMod2.get()))

options()
cmdGo = Button(window, width = 23, text = "Create Lists",font = ("Calibri","26","bold"), command = lambda:go(initial = True))
cmdGo.place(x = 25, y = 410)
mainloop()
