# Author: Jackie Xu
# Date: 12/10/2014
# Purpose: To create a fraction class which simulates a rational fraction
#========================================================================

import random
from tkinter import*

root = Tk(className = " Fractions")
root.config(width = 800, height = 600)

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

# Author: Jackie Xu
# Date: 12/11/2014
# Purpose: A class of for a fraction
# Fields: Numerator, Denominator
# Methods
# calcGCD: calculates and returns the greatest common factor between denominator and numerator
# reduce: Reduces the fraction to simpliest form
# setValue: Changes the value of the fraction
# randomize: Randomizes the fraction to a valid value within a given range
# __str__: formats fraction to a printable string
# calcInverse: Calculates the inverse of it self, inverse of 0 is protected from
# __eq__: returns true if itself is equal to another given fraction
# __add__: returns the sum of itself and a given faction
# __sub__: returns the difference of itself and a given fraction
# __mul__: returns the product of itself and a given fraction
# __truediv__: returns the quotient of itself and a given fraction, division by 0 is protected from

class Fraction:

    # Author: Jackie Xu
    # Date: 12/11/2014
    # Purpose: The constructor for the fraction class
    # Parameters: Self
    # Return Value: -

    def __init__(self,numer = 0,deno = 1):
        if deno == 0:
            self.intNumer = 0
            self.intDeno = 1
        else:
            self.intNumer = numer
            self.intDeno = deno
        self.reduce()

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 9/30/2014
    # Purpose: Calculates the great common factor (divisor)
    # Parameters: self
    # Return Value: n, greatest common factor

    def calcGCD(self):
        m = self.intNumer
        n = self.intDeno
        
        if n != 0 and m != 0:
            t = m % n
            while t != 0:
                m = n
                n = t
                t = m % n
        else:
            if n == 0 and m != 0:
                n = m
        return n

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/11/2014
    # Purpose: Reduces fraction to simplest formm
    # Parameters: self
    # Return Value: -

    def reduce(self):
        if self.intDeno == 0:
            self.intDeno = 1
            self.intNumer = 0
            print("Defaulted for 0 in deno(Reduce)")
        else:
            if self.calcGCD() != 1:
                gCD = self.calcGCD()
                self.intNumer = int(self.intNumer / gCD)
                self.intDeno = int(self.intDeno / gCD)

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/11/2014
    # Purpose: Sets the value of the fraction
    # Parameters: self,numerator, denominator
    # Return Value: -

    def setValue(self,numer = 1,deno = 1):

        self.intNumer = numer
        self.intDeno = deno
        self.reduce()

        

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/12/2014
    # Purpose: Randomizes to a valid fraction
    # Parameters: self
    # Return Value: -

    def randomize(self):
        self.intNumer = random.randint(-10,10)
        self.intDeno = random.randint(-10,10)
        while self.intDeno == 0:
            self.intDeno = random.randint(-10,10)
            
    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/11/2014
    # Purpose: Converts fraction into a string
    # Parameters: self
    # Return Value: -

    def __str__(self):
        self.reduce()
        if self.intDeno == 1:
            fraction = str(self.intNumer)
        else:
            if abs(self.intNumer) > abs(self.intDeno):
                whole = abs(self.intNumer) // self.intDeno
                if self.intNumer < 0:
                    whole = whole * -1
                top = abs(self.intNumer) - abs(whole) * abs(self.intDeno)
                fraction = str(whole) + " " + str(top) + "/" + str(self.intDeno)
            else:
                fraction = str(self.intNumer) + "/" + str(self.intDeno)
        return fraction

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/12/2014
    # Purpose: Calculates the inverse of the fraction
    # Parameters: self
    # Return Value: -

    def calcInverse(self):
        inverse = Fraction(self.intDeno,self.intNumer)
        return inverse

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/12/2014
    # Purpose: Determines if a given fraction is equal to it
    # Parameters: self, 2ndFraction
    # Return Value: -

    def __eq__(self,secondFraction):
        equal = False
        if self.intNumer == secondFraction.intNumer and \
                           self.intDeno == secondFraction.intDeno:
            equal = True
        return equal

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/12/2014
    # Purpose: returns the sum of a fraction and itself
    # Parameters: self, 2ndFraction
    # Return Value: -

    def __add__(self,secondFraction):
        answer = Fraction()
        answer.intNumer = self.intNumer * secondFraction.intDeno + self.intDeno \
                          * secondFraction.intNumer
        answer.intDeno = self.intDeno * secondFraction.intDeno
        return answer

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/12/2014
    # Purpose: returns the difference of a fraction and itself
    # Parameters: self, 2ndFraction
    # Return Value: -

    def __sub__(self,secondFraction):
        answer = Fraction()
        answer.intNumer = self.intNumer * secondFraction.intDeno - self.intDeno \
                          * secondFraction.intNumer
        answer.intDeno = self.intDeno * secondFraction.intDeno
        return answer

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/16/2014
    # Purpose: returns the product of a fraction and itself
    # Parameters: self, 2ndFraction
    # Return Value: -

    def __mul__(self,secondFraction):
        answer = Fraction()
        answer.intNumer = self.intNumer * secondFraction.intNumer
        answer.intDeno = self.intDeno * secondFraction.intDeno
        return answer

    #-------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/16/2014
    # Purpose: returns the quotient of a fraction and itself
    # Parameters: self, 2ndFraction
    # Return Value: -
    
    def __truediv__(self,secondFraction):
        answer = Fraction()
        answer.intNumer = self.intNumer * secondFraction.intDeno
        answer.intDeno = self.intDeno * secondFraction.intNumer
        return answer

#-------------------------------------------------------
# Author: Jackie Xu
# Date: 12/16/2014
# Purpose: Starts the main game
# Parameters: first,test,operator
# Return Value: -

def go(first = False,test = False,operator = 1):
    global correct
    global sign
    global fraction1
    global fraction2
    global ans
    global realAns
    
    global totalQuestion
    global correctScore
    global currentQuestion
    global maxQuestion
    
    if first:
        currentQuestion = 0
        totalQuestion = 0
        correctScore = 0

        window.create_rectangle(0,600,800,430, fill = "Khaki", outline = "Khaki")

        cmdStart.place_forget()
        cmdCorrect.place(x = 10, y = 300)
        cmdWrong.place(x = 600, y = 300)

    cmdNext.place_forget()
    cmdChoose.place_forget()
    cmdCorrect.config(state = NORMAL)
    cmdWrong.config(state = NORMAL)

    if test == False:
        fraction1.randomize()
        fraction2.randomize()
        operator = random.randint(1,4)
        
    if operator == 1:
        realAns = fraction1 + fraction2
        sign = " + "
    elif operator == 2:
        realAns = fraction1 - fraction2
        sign = " - "
    elif operator == 3:
        realAns = fraction1 * fraction2
        sign = " × "
    else:
        realAns = fraction1 / fraction2
        while fraction2.intNumer == 0:
            print("Can't divide by 0, fraction 2 has been re-randomized")
            fraction2.randomize()
            realAns = fraction1 / fraction2
        sign = " ÷ "

    print("Fraction1 = " + str(fraction1))
    print("Fraction2 = " + str(fraction2))
    print()
    print("Real answer = " + str(realAns))
    print()

    

    window.create_rectangle(0,100,800,430, fill = "Khaki", outline = "Khaki")
    window.create_rectangle(0,100,800,300, fill = "SandyBrown", outline = "SandyBrown")
    
    if test:
        window.create_text(20, 120, anchor = W, text = "Valid Test inputs imported", font = ("Calibri","20","bold"))
    else:
        window.create_text(20, 120, anchor = W, text = "Question: ", font = ("Calibri","20","bold"))
        window.create_text(160, 120, anchor = W, text = str(currentQuestion + 1) + "/" + str(maxQuestion), font = ("Calibri","24","bold"))


    ranAns = random.randint(0,1)


    ans = realAns

    correct = True
    
    if ranAns == 0:
        ans = realAns.calcInverse()
        correct = False

        if ans == realAns:
            correct = True

    window.create_text(20, 200, anchor = W, text = str(fraction1) + str(sign) + str(fraction2) + \
                       " = " + str(ans), font = ("Calibri","40","bold"))



#-------------------------------------------------------
# Author: Jackie Xu
# Date: 12/17/2014
# Purpose: Counts score and decides whether it's right or wrong
# Parameters: answer
# Return Value: -

def check(answer):
    global correctScore
    global totalQuestion
    global currentQuestion
    global maxQuestion

    cmdCorrect.config(state = DISABLED)
    cmdWrong.config(state = DISABLED)

    window.create_rectangle(0,600,800,430, fill = "Khaki", outline = "Khaki")

    currentQuestion = currentQuestion + 1
    
    if (answer == True and correct) or (answer == False and not correct):
        window.create_text(20, 400, anchor = W, text = "Yes! " + str(realAns) + \
                       " is the correct answer.", font = ("Calibri","40","bold"))
        correctScore = correctScore + 1
        print("YES!")
    else:
        window.create_text(20, 400, anchor = W, text = "Nope! " + str(realAns) + \
                       " is the correct answer.", font = ("Calibri","40","bold"))
        print("NUUUU")
    totalQuestion = totalQuestion + 1

    window.create_text(20, 470, anchor = W, text = "Total score: " + str(correctScore) + \
                       " / " + str(totalQuestion), font = ("Calibri","40","bold"))

    print(str(fraction1) + str(sign) + str(fraction2))
    print(realAns)
    print()

    if currentQuestion >= maxQuestion:
        score = correctScore / totalQuestion * 100
        score = round(score,1)
        window.create_text(20, 550, anchor = W, text = "Your final mark is: " + str(score) + \
               "%", font = ("Calibri","40","bold","underline"))
        print("DONE")
        cmdRestart.place(x = 300,y = 320)
    else:
        cmdNext.place(x = 260,y = 300)

#-------------------------------------------------------
# Author: Jackie Xu
# Date: 12/18/2014
# Purpose: Counts score and decides whether it's right or wrong
# Parameters: -
# Return Value: -

def test():
    global fraction1
    global fraction2

    fraction1.setValue(3,7)
    fraction2.setValue(-7,3)
    
    go(test = True,operator = 4)

#-------------------------------------------------------
# Author: Jackie Xu
# Date: 12/19/2014
# Purpose: Sets the number of questions
# Parameters: -
# Return Value: -

def setNumber():
    global widget
    global new
        
    new = Toplevel(window,width = 400,height = 100)
    prompt = Canvas(new,width = 400, height = 100,bg = "white")
    prompt.place(x = 0, y = 0)

    prompt.create_text(10, 20, anchor = W, text = "Please set the amount of questions: ", \
                       font = ("Calibri","16","bold"))

    widget = Scale(new,from_ = 5, to = 30, resolution = 1,length = 250,orient = HORIZONTAL, \
                   bg = "white",font = ("Calibri","20","bold"))
    widget.place(x = 10, y = 30)
    widget.set(10)

    ok = Button(new,text = "Set", width = 8, height = 2,font = ("Calibri","14","bold"),command = lambda:set())
    ok.place(x = 280, y = 30)

#-------------------------------------------------------
# Author: Jackie Xu
# Date: 12/19/2014
# Purpose: Command for the setNumber button
# Parameters: -
# Return Value: -

def set():
    global maxQuestion
    maxQuestion = widget.get()
    new.destroy()

    currentQuestion = 0
    totalQuestion = 0
    correctScore = 0

    cmdCorrect.place_forget()
    cmdWrong.place_forget()
    cmdNext.place_forget()
    cmdStart.place(x = 100,y = 300)

    window.create_rectangle(0,100,800,600, fill = "Khaki", outline = "Khaki")

    window.create_text(100, 200, anchor = W, text = "Number of questions: " + str(maxQuestion), font = ("Calibri","40","bold"))

#-------------------------------------------------------
# Author: Jackie Xu
# Date: 1/5/2015
# Purpose: Resets the game
# Parameters: -
# Return Value: -

def restart():
    cmdCorrect.place_forget()
    cmdWrong.place_forget()
    cmdRestart.place_forget()
    cmdNext.place_forget()
    
    window.create_rectangle(0,100,800,600, fill = "Khaki", outline = "Khaki")
    cmdStart.place(x = 100,y = 300)
    cmdChoose.place(x = 400,y = 300)
    window.create_text(100, 200, anchor = W, text = "Number of questions: " + str(maxQuestion), font = ("Calibri","40","bold"))

#MAIN===========================================================================
window = Canvas(root,width = 800, height = 600,bg = "Khaki")
window.place(x = 0,y = 0)
maxQuestion = 10
#Menu--------
menubar = Menu(root)

startMenu = Menu(menubar,tearoff = 0)
startMenu2 = Menu(menubar,tearoff = 0)

startMenu2.add_command(label = "New Game", command = lambda:restart())
startMenu2.add_command(label = "Set number of questions", command = lambda:setNumber())
startMenu.add_command(label = "Help", command = lambda:help())
startMenu.add_command(label = "TEST MODE", command = lambda:test())

startMenu.add_separator()
startMenu.add_command(label = "Exit", command = lambda:root.destroy())

menubar.add_cascade(label = "Game", menu = startMenu2)
menubar.add_cascade(label = "Options", menu = startMenu)

root.config(menu = menubar)
#-----------------------------

fraction1 = Fraction()
fraction2 = Fraction()

right = 0
all = 0

window.create_text(25, 50, anchor = W, text = "Fractions", font = ("Calibri","36","bold"))
window.create_text(25, 200, anchor = W, text = "Welcome to Fractions! This is a quiz simulator to test your skills with fractions!", font = ("Calibri","16","bold"))
window.create_text(25, 220, anchor = W, text = "Start by choosing how many questions you want to then click 'Start!'", font = ("Calibri","16","bold"))
window.create_text(100, 400, anchor = W, text = "Number of questions: " + str(maxQuestion), font = ("Calibri","40","bold"))


cmdStart = Button(window, text = "Start!", width = 10, font = ("Calibri","18","bold"),command = lambda: go(first = True))
cmdStart.place(x = 100,y = 300)

cmdRestart = Button(window, text = "Replay!", width = 10, font = ("Calibri","18","bold"),command = lambda: restart())

cmdChoose = Button(window, text = "Set amount of questions", width = 26, font = ("Calibri","18","bold"),command = lambda: setNumber())
cmdChoose.place(x = 400,y = 300)

cmdCorrect = Button(window, text = "Correct", width = 10, font = ("Calibri","24","bold"),command = lambda: check(answer = True))
cmdWrong = Button(window, text = "Wrong", width = 10, font = ("Calibri","24","bold"),command = lambda: check(answer = False))
cmdNext = Button(window, text = "Next question", width = 16, font = ("Calibri","24","bold"),command = lambda: go())

mainloop()


