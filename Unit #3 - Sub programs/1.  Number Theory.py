# Author: Jackie Xu
# Date: 9/20/2014
# Purpose: To break down big problems with sub programs
#----------------------------------------------------------------------------

# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: A function that gets user input in range of (low,high)
# Parameters: Range of valid inputs(Low,High)
# Return Value: Valid user integer

def getPositiveInteger(Low = 0,High = 100):
    blnOK = False
    strNum = ""
    strPrompt = "Please enter a positive integer between " + str(Low) + " and " + str(High) + ": "

    while not strNum.isdigit() or not blnOK:

        strNum = input(strPrompt)
        if strNum.isdigit():
            intNum = int(strNum)
            if intNum <= High and intNum >= Low:
                blnOK = True
            else:
                print("Your number is out of range!")
                
        else:
            print("You did not enter a NUMBER!")
    return intNum
#----------------------------------------------------------------------------



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
        Temp = n
        n = r
        r = Temp
    Permutations = calcFactorial(n) / calcFactorial((n - r))
    return int(Permutations)
#----------------------------------------------------------------------------


# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: Combination calculation function
# Parameters: n number of objects taking r at a time, n >= r, n >= 0
# Return Value: Number of combinations

def calcCombinations(n,r):
    if r > n:
        Temp = n
        n = r
        r = Temp
    Combinations = calcFactorial(n) / (calcFactorial(r)* calcFactorial((n - r)))
    return int(Combinations)
#----------------------------------------------------------------------------


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
        if n == 0 and m != 0:
            n = m
    return n
#----------------------------------------------------------------------------


# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: function for calculating least common multiple
# Parameters:m,n, which are positive integers
# Return Value: LCM

def calcLCM(m,n):
    if calcGCD(m,n) != 0:
        LCM = m * n / calcGCD(m,n)
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
    isRP = False
    if calcGCD(m,n) == 1:
        isRP = True
    else:
        RP = False
    return isRP
    
#----------------------------------------------------------------------------


# Main
strStart = "Y"
while strStart == "Y":
    Input1 = getPositiveInteger(0,100)
    Input2 = getPositiveInteger(0,100)
    print()
    print("Number of Permutations",calcPermutations(Input1,Input2))
    print("Number of Combinations",calcCombinations(Input1,Input2))
    if calcGCD(Input1,Input2) == 0:
        print("The greatest common factor is any natural number")
    else:
        print("The greatest common factor is",calcGCD(Input1,Input2))
    print("The least common multiple is",calcLCM(Input1,Input2))
    if isRelativelyPrime(Input1,Input2):
        print(Input1,"and",Input2,"are relatively prime")
    else:
        print(Input1,"and",Input2,"are not relatively prime")
    print()
    strStart = input("Type 'Y' to start again ")
    print()
