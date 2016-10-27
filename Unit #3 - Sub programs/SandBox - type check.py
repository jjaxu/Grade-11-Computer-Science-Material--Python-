# Author: Jackie Xu
# Date: 10/1/2014
# Purpose: Sandbox - Functions and type check
#--------------------------------------------

def getNumber(low = 1,high = 100):
    blnOK = False
    strNumber = ""
    
    strNumber = input("Enter a number between " + str(low) + " and " + str(high) + ": ")
    while (not strNumber.isdigit()):
        print("BAD INPUT! NOT NUMBER!")
        strNumber = input("Enter a number : ")
    side = int(strNumber)
    return side
#--------------------------------------------
low = 1
high = 100

sideA = getNumber(low,high)
sideB = getNumber(low,high)
sideC = getNumber(low,high)
