# Author: Jackie Xu
# Date: 9/16/2014
# Purpose: To explore more build in functions in python (Digits.py)
#-------------------------------------------------------------------------------

while input("Start? (Y/N)") == "Y":

    # Number of digits in the number
    Digit = 1
    OrgNum = int(input("Please enter a positive integer: "))
    while OrgNum < 0:
        OrgNum = int(input("Please re-enter a POSITIVE integer: "))
    NewNum = OrgNum

    while NewNum // 10 != 0:
        NewNum = NewNum // 10
        Digit = Digit + 1
    print("Number of digits:",Digit)

    # Sum of digits in the number
    Count = OrgNum // 10
    Sum = 0
    Remainder = OrgNum
    NewNum = OrgNum

    while Count + 1!= 0:
        Remainder = NewNum % 10
        NewNum = NewNum // 10
        Sum = Sum + Remainder
        Count = Count - 1
    print("Sum of digits is:",Sum)

    # Reverse of the number
    Count = OrgNum // 10
    NewNum = OrgNum
    Reverse = 0

    while Count + 1 != 0:
        Remainder = int(NewNum % 10 * (10 ** (Digit - 1)))
        NewNum = NewNum // 10
        Count = Count - 1
        Digit = Digit - 1
        Reverse = Reverse + Remainder
    print("Reverse is",Reverse)

    # Palindrom test
    if Reverse == OrgNum:
        print(OrgNum,"is a palindrom")
    else:
        print(OrgNum,"is not a palindrom")
    print()
    
