# Author: Jackie Xu
# Date: 12/2/2014
# Purpose: To work with composition of classes, which is classes within other classes
# ===================================================================================

import random
from tkinter import*

root = Tk(className = " Dices")
root.config(width = 600, height = 450)

strValue = StringVar()
intSize = IntVar()
intRadius = IntVar()
intGap = IntVar()

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

#--------------------------------------------------------------
# Author: Jackie Xu
# Date: 12/2/2014
# Purpose: Creates a dice class with characteristics of a dice
# Parameters: value, size, radius, gap
# Return: __str__, getValue, setValue, setSize, roll, draw

class Dice:

    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: The constructor for the Dice class
    # Parameters: value, size, radius, gap
    # Return: __str__, getValue, setValue, setSize, roll, draw

    def __init__(self,value = "",size = 50,radius = 0,gap = 0):

        if not bobRangeCheck(str(value),1,6):
            #print("Randomized as default")
            #print()
            value = random.randint(1,6)
       # size = value
        radius = size / 5
        gap = radius / 2

        self.value = value
        self.size = size
        self.radius = radius
        self.gap = gap

    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: Returns the value of the dice as a string
    # Parameters: self
    # Return: value as a string

    def __str__(self):
        return str(self.value)

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: gets the value of the die from the user
    # Parameters: self
    # Return: -

    def getValue(self):
        userInput = input("Plese enter value of the dice: ")
        if bobRangeCheck(userInput,1,6):
            self.value = int(userInput)
        else:
            self.setValue()
            print("ERROR, Value not between 1 - 6")
            print("Defaulted to 1")
            print()

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: sets the value of the dice
    # Parameters: self
    # Return: -

    def setValue(self,value = 1):
        if bobRangeCheck(str(value),1,6):
            self.value = value
        else:
            self.value = 1
            print("Defaulted for error (value = 1)")

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: sets the value of the dice
    # Parameters: self
    # Return: -

    def setSize(self,size = 50):
        if bobRangeCheck(str(size),30,100):
            self.size = int(size)
        else:
            self.size = 50
            print("Defaulted for error (size = 50)")

        self.radius = self.size / 5
        self.gap = self.radius / 2

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: randomly set the dice to a new valid value
    # Parameters: self
    # Return: -

    def roll(self):
        self.value = random.randint(1,6)

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/2/2014
    # Purpose: draws the dice
    # Parameters: self
    # Return: -

    def draw(self,canvas,x,y):
        canvas.create_rectangle(x,y,x + self.size,y + self.size,fill = "white")

        if not self.value == 1:
            canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.radius, y + self.gap + self.radius,fill = "black")
            canvas.create_oval(x + 3 * self.gap + 2 * self.radius , y + 3 * self.gap + 2 * self.radius , \
                               x + 3 * self.gap + 3 * self.radius,  y + 3 * self.gap + 3 * self.radius, fill = "black")
            if not self.value == 2 and self.value % 2 == 0:
                canvas.create_oval(x + 3 * self.gap + 2 * self.radius , y + self.gap, \
                                   x + 3 * self.gap + 3 * self.radius,  y + self.gap + self.radius, fill = "black")
                canvas.create_oval(x + self.gap, y + 3 * self.gap + 2 * self.radius, \
                                   x + self.gap + self.radius, y + 3 * self.gap + 3 * self.radius, fill = "black")
                if self.value == 6:
                    canvas.create_oval(x + self.gap ,y + 2 * self.gap + self.radius, \
                                       x + self.gap +self.radius,  y + 2 * self.gap + 2 * self.radius, fill = "black")
                    canvas.create_oval(x + 3 * self.gap + 2 * self.radius, y + 2 * self.gap + self.radius, \
                                       x + 3 * self.gap + 3 * self.radius, y + 2 * self.gap + 2 * self.radius, fill = "black")
            elif not self.value == 2:
                canvas.create_oval(x + 2 * self.gap + self.radius, y + 2 * self.gap + self.radius, \
                               x + 2 * self.gap + 2 * self.radius, y + 2 * self.gap + 2 * self.radius,fill = "black")
                if self.value == 5:
                    canvas.create_oval(x + 3 * self.gap + 2 * self.radius , y + self.gap, \
                                       x + 3 * self.gap + 3 * self.radius,  y + self.gap + self.radius, fill = "black")
                    canvas.create_oval(x + self.gap, y + 3 * self.gap + 2 * self.radius, \
                                       x + self.gap + self.radius, y + 3 * self.gap + 3 * self.radius, fill = "black")
            
                
        else:
            canvas.create_oval(x + 2 * self.gap + self.radius, y + 2 * self.gap + self.radius, \
                               x + 2 * self.gap + 2 * self.radius, y + 2 * self.gap + 2 * self.radius,fill = "black")
            

#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/4/2014
# Purpose: To create a superclass with Dice classes as it's fields
# Parameters: Dice1, Dice2, Dice2 (each is a dice class)
# Return: -

class Hand:
    
    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/4/2014
    # Purpose: To create a superclass with Dice classes as it's fields
    # Parameters: Dice1, Dice2, Dice2 (each is a dice class)
    # Return: -

    def __init__(self,handSize = 50):
        
        self.firstDie = Dice(size = handSize)
        self.secondDie = Dice(size = handSize)
        self.thirdDie = Dice(size = handSize)

        self.sort()
        

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/4/2014
    # Purpose: Converts the super class into a simple string
    # Parameters: self
    # Return: Dices as string

    def __str__(self):
        self.sort()
        return self.firstDie.__str__() + "-" + self.secondDie.__str__() + "-" + self.thirdDie.__str__()

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/4/2014
    # Purpose: Gets value of hands from the user and varifies it
    # Parameters: self
    # Return: -

    def getValues(self):
        
        #self.firstDie = Dice(value = self.firstDie.getValue())
        #self.secondDie = Dice(value = self.secondDie.getValue())
        #self.thirdDie = Dice(value = self.thirdDie.getValue())

        self.firstDie.getValue()
        self.secondDie.getValue()
        self.thirdDie.getValue()

        self.sort()

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/4/2014
    # Purpose: Sets size of the entire hand
    # Parameters: self
    # Return: -

    def setSize(self,handSize = 50):
        
        self.firstDie.setSize(handSize)
        self.secondDie.setSize(handSize)
        self.thirdDie.setSize(handSize)

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/5/2014
    # Purpose: Sorts the hand from smallest to largest
    # Parameters: self
    # Return: -

    def sort(self):
        a = self.firstDie.value
        b = self.secondDie.value
        c = self.thirdDie.value

        if a <= b and a <= c:
            self.firstDie.value = a
            if b <= c:
                self.secondDie.value = b
                self.thirdDie.value = c
            else:
                self.secondDie.value = c
                self.thirdDie.value = b
                
        elif b <= a and b <= c:
            self.firstDie.value = b
            if a <= c:
                self.secondDie.value = a
                self.thirdDie.value = c
            else:
                self.secondDie.value = c
                self.thirdDie.value = a
        else:
            self.firstDie.value = c
            if a <= b:
                self.secondDie.value = a
                self.thirdDie.value = b
            else:
                self.secondDie.value = b
                self.thirdDie.value = a

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/5/2014
    # Purpose: rolls the entire hand
    # Parameters: self
    # Return: -

    def roll(self):
        self.firstDie.roll()
        self.secondDie.roll()
        self.thirdDie.roll()
        self.sort()

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/5/2014
    # Purpose: draws the hand on a canvas
    # Parameters: self
    # Return: -

    def draw(self,x,y):
        self.firstDie.draw(window,x,y)
        self.secondDie.draw(window,x + self.firstDie.size,y)
        self.thirdDie.draw(window, x + 2 * self.firstDie.size,y)

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/5/2014
    # Purpose: determines if the hand is a win
    # Parameters: self
    # Return: True/False

    def isWinner(self):
        win = False
        
        first = self.firstDie.value
        second = self.secondDie.value
        third = self.thirdDie.value

        if first == 4 and second == 5 and third == 6:
            win = True
        elif first == second and first == third:
            win = True
        elif first == second and third == 6:
            win = True
        return win

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/5/2014
    # Purpose: determines if the hand is a lose
    # Parameters: self
    # Return: True/False

    def isLoser(self):
        lose = False

        first = self.firstDie.value
        second = self.secondDie.value
        third = self.thirdDie.value

        if first == 1 and second == 2 and third == 3:
            lose = True
        elif first == 1 and second != 1 and second == third:
            lose = True
        return lose

    #---------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/8/2014
    # Purpose: Calculates the number of points earned
    # Parameters: self
    # Return: points

    def calcPoint(self):
        self.sort()
        first = self.firstDie.value
        second = self.secondDie.value
        third = self.thirdDie.value
        points = 0
        
        if not(self.isWinner() or self.isLoser()):
            if first == second:
                points = third
            elif second == third and first < second:
                points = first
        return points
           

    

#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/5/2014
# Purpose: dice tester, choose you own values
# Parameters: -
# Return: -

def test():
    myHand.getValues()
    #myHand.sort()
    go("Test")
#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/5/2014
# Purpose: Displays a hand
# Parameters: -
# Return: -

def go(mode = "Single"):

    window.create_rectangle(0,100,800,600, fill = "SandyBrown", outline = "SandyBrown")
    
    if mode != "Test":
        myHand.roll()
    else:
        window.create_text(25, 350, anchor = W, text = "Test values imported", font = ("Calibri","20","bold"))


        
    if myHand.isWinner():
        window.create_text(25, 300, anchor = W, text = "This hand is a Win!", font = ("Calibri","20","bold"))
    elif myHand.isLoser():
        window.create_text(25, 300, anchor = W, text = "This hand is a Lose!", font = ("Calibri","20","bold"))
    else:
        if myHand.calcPoint() == 0:
            window.create_text(25, 300, anchor = W, text = "This hand is Nothing!", font = ("Calibri","20","bold"))
        else:
            print(myHand.calcPoint())
            window.create_text(25, 300, anchor = W, text = "This hand wins you " + \
                               str(myHand.calcPoint()) + " points!", font = ("Calibri","20","bold"))            

    myHand.draw(20,100)

#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/9/2014
# Purpose: Prints instructions of the dice game
# Parameters: -
# Return: -

def help():
    print()
    print("Instructions:")
    print("Click 'Create Hand' will create a hand of 3 dices. " + \
          "Then it determines whether if the hand is a win, lose, neither, or points gained. " + \
          "You can also click 'Run Simulation' button to generate 10,000 hands and it will automatically tally up the wins, loses, neithers and points.")
    print()


#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/9/2014
# Purpose: Runs the simulation of 10000 hands
# Parameters: -
# Return: -

def simulate():
    win = 0
    lose = 0
    nothing = 0
    points = 0

    window.create_rectangle(0,100,800,600, fill = "SandyBrown", outline = "SandyBrown")
    
    for count in range(1,10001):
        myHand.roll()
        if myHand.isWinner():
            win = win + 1
        elif myHand.isLoser():
            lose = lose + 1
        elif myHand.calcPoint() == 0:
            nothing = nothing + 1
        else:
            points = points + myHand.calcPoint()

    window.create_text(300, 130, anchor = W, text = "Wins: " + str(win), font = ("Calibri","20","bold"))
    window.create_text(300, 180, anchor = W, text = "Loses: " + str(lose), font = ("Calibri","20","bold"))
    window.create_text(300, 230, anchor = W, text = "Nothings: " + str(nothing), font = ("Calibri","20","bold"))
    window.create_text(300, 280, anchor = W, text = "Points: " + str(points), font = ("Calibri","20","bold"))

    window.create_text(25, 350, anchor = W, text = "A simulation of 10,000 hands is complete", \
                       font = ("Calibri","15","bold"))
    
#---------------------------------------------------
# Author: Jackie Xu
# Date: 12/10/2014
# Purpose: Sets the dice's size
# Parameters: -
# Return: -

def setSize():
    userInput = input("Please choose your handsize (30-100): ")
    myHand.setSize(userInput)
    window.create_rectangle(0,100,800,600, fill = "SandyBrown", outline = "SandyBrown")

    print("Size has been set to " + str(myHand.firstDie.size))
    window.create_text(25, 350, anchor = W, text = "Hand size has been set to " + str(myHand.firstDie.size), \
                       font = ("Calibri","15","bold"))
        
#MAIN===========================================================================
window = Canvas(root,width = 600, height = 450,bg = "SandyBrown")
window.place(x = 0,y = 0)

#Menu--------
menubar = Menu(root)

startMenu = Menu(menubar,tearoff = 0)
startMenu2 = Menu(menubar,tearoff = 0)

startMenu2.add_command(label = "New Hand", command = lambda:go())
startMenu2.add_command(label = "Run Simulation", command = lambda:simulate())

startMenu.add_command(label = "Help", command = lambda:help())
startMenu.add_command(label = "Set hand size", command = lambda:setSize())
startMenu.add_command(label = "TEST MODE", command = lambda:test())

startMenu.add_separator()
startMenu.add_command(label = "Exit", command = lambda:root.destroy())

menubar.add_cascade(label = "Game", menu = startMenu2)
menubar.add_cascade(label = "Dice Options", menu = startMenu)

root.config(menu = menubar)

window.create_text(25, 50, anchor = W, text = "Dices ", font = ("Calibri","36","bold"))
window.create_text(20, 350, anchor = W, text = "Welcome to the Dice game, you can find help inside the options tab.", font = ("Calibri","15","bold"))

#-------------
myHand = Hand()
myHand.setSize(handSize = 100)

cmdHand = Button(window, text = "Create Hand", width = 10, font = ("Calibri","18","bold"),command = lambda: go())
cmdHand.place(x = 15,y = 375)

cmdSimulate = Button(window, text = "Run Simulation", width = 14, font = ("Calibri","18","bold"),command = lambda: simulate())
cmdSimulate.place(x = 400,y = 375)

mainloop()

