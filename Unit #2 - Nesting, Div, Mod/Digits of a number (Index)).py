# Author: Jackie Xu
# Date: 9/16/2014
# Purpose: To explore more build in functions in python (Digits.py)
#-------------------------------------------------------------------------------

while input("Start? (Y/N)") == "Y":

    # Number of digits in the number
    Num = input("Please enter a positive integer: ")
    while int(Num)< 0:
        Num = input("Please re-enter a POSITIVE integer: ")
    
    print("Number of digits:",len(str(Num)))

    # Sum of digits
    Count = 0
    Sum = 0
    while Count != len(str(Num)):
        Digit = int(Num[Count:Count + 1])
        Count = Count + 1
        Sum = Sum + Digit
    print("Sum of digits:",Sum)

    # Reverse of the number
    Digit = ""
    Reverse = ""
    Count = 0
    Length = len(Num)
    
    while Count != len(Num):
        Digit = Num[Length - 1:Length]
        Count = Count + 1
        Length = Length - 1
        Reverse = Reverse + Digit

    print("Reverse of number:",Reverse)
