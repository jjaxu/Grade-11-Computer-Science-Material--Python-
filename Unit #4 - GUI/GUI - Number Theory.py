# Author: Jackie Xu
# Date: 11/3/2014
# Purpose: Turning The Number theory program into a GUI
#-------------------------------------------------------------------

from tkinter import*
root = Tk(className = " GUI - Number Theory")

# Declare
input1 = StringVar()
input2 = StringVar()

permutations = IntVar()
combinations = IntVar()
gcd = IntVar()
lcm = IntVar()
isRP = StringVar()

# Init'
input1.set(value = "")
input2.set(value = "")

permutations.set(value = 0)
combinations.set(value = 0)
gcd.set(value = 0)
lcm.set(value = 0)
isRP.set(value = "Yes")

#=====================================================================
# Author: Jackie Xu
# Date: 11/6/2014
# Purpose: "Bob" check function
# Parameters: String input
# Return Value: True/False

def bobRangeCheck(strInput,low = 0,high = 100):
    ok = False
    if strInput.isdigit():
        if int(strInput) >= 0 and int(strInput) <= 100:
            ok = True
    return ok

# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Writing a factorial function
# Parameters: Positive Integer input
# Return Value: Factorial of that number

def calcFactorial(Int):
    Factorial = 1
    for Count in range(1,Int+1):
        Factorial = Factorial * Int
        Int = Int - 1
    return Factorial

#----------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Permutation calculating function
# Parameters: n number of objects taking r at a time, n >= r, n >= 0
# Return Value: Number of permutations

def calcPermutations(n,r):
    if r > n:
        r,n = n,r
    Permutations = calcFactorial(n) / calcFactorial((n - r))
    return int(Permutations)

# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Combination calculation function
# Parameters: n number of objects taking r at a time, n >= r, n >= 0
# Return Value: Number of combinations

def calcCombinations(n,r):
    if r > n:
        r,n = n,r
    Combinations = calcFactorial(n) / (calcFactorial(r)* calcFactorial((n - r)))
    return int(Combinations)

# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Calculates the great common factor (divisor)
# Parameters: m,n, which are postive integers
# Return Value: n, greatest common factor

def calcGCD(m,n):
    if n != 0 and m != 0:
        t = m % n
        while t != 0:
            m = n
            n = t
            t = m % n
    else:
        if (n == 0 and m != 0) or (m == 0 and n != 0):
            n = m
        else:
            n = "any natural number"
    return n
#----------------------------------------------------------------------------

# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: function for calculating least common multiple
# Parameters:m,n, which are positive integers
# Return Value: LCM

def calcLCM(m,n):
    if str(calcGCD(m,n)).isdigit():
        if calcGCD(m,n) != 0:
            LCM = m * n / calcGCD(m,n)
        else:
            LCM = 0
    else:
        LCM = 0
    return int(LCM)

#----------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Function for relatively prime for 2 integers
# Parameters: m,n, positive intergers
# Return Value: True or False

def isRelativelyPrime(m,n):
    isRP = "No"
    if calcGCD(m,n) == 1:
        isRP = "Yes"
    else:
        RP = "No"
    return isRP
#----------------------------------------------------------------------------

def calculate(int1, int2):
    lblPerm.grid(row = 5, column = 0, sticky= W, padx = 5, pady = 5)
    lblComb.grid(row = 6, column = 0, sticky= W, padx = 5, pady = 5)
    lblGCD.grid(row = 7, column = 0, sticky= W, padx = 5, pady = 5)
    lblLCM.grid(row = 8, column = 0, sticky= W, padx = 5, pady = 5)
    lblRP.grid(row = 9, column = 0, sticky= W, padx = 5, pady = 5)

    if bobRangeCheck(int1) and bobRangeCheck(int2):
        int1 = int(int1)
        int2 = int(int2)
    
        permutations.set("Number of Permuations: " + str(calcPermutations(int1,int2)))
        combinations.set("Number of Combinations: " + str(calcCombinations(int1,int2)))
        gcd.set("Greatest common factor: " + str(calcGCD(int1,int2)))
        lcm.set("Least Common Multiple: " + str(calcLCM(int1,int2)))
        isRP.set("Are the numbers Relatively Prime? " + str(isRelativelyPrime(int1,int2)))

    else:
        clearObj()
        lblPerm.grid(row = 5, column = 0, sticky= W, padx = 5, pady = 5)
        permutations.set("You either did not enter numbers or your numbers are out of range!")
        

def clearObj():
    lblPerm.grid_remove()
    lblComb.grid_remove()
    lblGCD.grid_remove()
    lblLCM.grid_remove()
    lblRP.grid_remove()

    input1.set("")
    input2.set("")
    
#GUI===========================================================================================================

#Menu--------
menubar = Menu(root)

startMenu = Menu(menubar,tearoff = 0)

startMenu.add_separator()
startMenu.add_command(label = "Exit", command = lambda:root.destroy())

menubar.add_cascade(label = "Menu", menu = startMenu)
root.config(menu = menubar)
#-------------

Label(root,text = "Number Theory").grid(row = 0, column = 0, sticky= W, padx = 5, pady = 5)
Label(root,text = "Integer 1: (0-100)").grid(row = 1, column = 0, sticky= W, padx = 5, pady = 5)
Label(root,text = "Integer 2: (0-100)").grid(row = 2, column = 0, sticky= W, padx = 5, pady = 5)

# Input
txtBox1 = Entry(root,textvariable = input1,width = 12).grid(row = 1, column = 1,sticky= W,padx = 5, pady = 5)
txtBox2 = Entry(root,textvariable = input2,width = 12).grid(row = 2, column = 1,sticky= W,padx = 5, pady = 5)

lblPerm = Label(root,textvariable = permutations)
lblComb = Label(root,textvariable = combinations)
lblGCD = Label(root,textvariable = gcd)
lblLCM = Label(root,textvariable = lcm)
lblRP = Label(root,textvariable = isRP)

# Process
Button(root,text = "Calculate", width = 10,height = 1,command = lambda:calculate(input1.get(),input2.get())).\
    grid(row = 4, column = 0,sticky= W,padx = 5, pady = 5)
Button(root,text = "Clear", width = 10,height = 1,command = lambda:clearObj()).\
    grid(row = 4, column = 1,sticky= W,padx = 5, pady = 5)

mainloop()
