# Author: Jackie Xu
# Date: 9/16/2014
# Purpose: To explore more build in functions in python (Digits.py)
#-------------------------------------------------------------------------------

strStart = "Y"
while strStart == "Y":
    OrgInput = int(input("Enter input a positive integer: "))
    TempInput = OrgInput
    Reverse = 0
    Sum = 0
    Digit = 0

    if TempInput == 0:
        Digit = 1
    
    while OrgInput < 0:
        OrgInput = int(input("Enter input a VALID integer: "))
        
    TempInput = OrgInput
    NewNum = TempInput
    
    while NewNum != 0:
        Digit = Digit + 1
        TempInput = NewNum
        Remainder = Reverse
        NewNum = TempInput // 10
        Remainder = TempInput % 10
        Sum = Sum + Remainder
        Reverse = Reverse * 10 + Remainder

    digiSum = 10
    TempInput2 = OrgInput
    Count = 0

    #Digital root
    while digiSum > 9 or Count != 20:
        Count = Count + 1
        digiSum = 0
        while 10 * TempInput2 // 10 != 0:
            NewNum2 = TempInput2 % 10
            TempInput2 = TempInput2 // 10
            digiSum = digiSum + NewNum2
        TempInput2 = digiSum

    print("Number of digits:",Digit)
    print("Sum of digits:",Sum)
    print("Reverse of number:",Reverse)
    print("Digital root is:",digiSum)
    if Reverse == OrgInput:
        print(OrgInput,"is a palindrome")
    else:
        print(OrgInput,"is a not palindrome")
    print()
    strStart = input("Enter 'Y' to start again ")
    print()
