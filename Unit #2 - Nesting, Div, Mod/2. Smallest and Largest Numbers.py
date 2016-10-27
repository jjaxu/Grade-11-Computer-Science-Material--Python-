# Author: Jackie Xu
# Date: 9/22/2014
# Purpose: More nesting. Using decisions inside loops (Nested decisions)
#-------------------------------------------------------------------------------

strStart = "Y"
while strStart == "Y":
    Count = 1
    Sum = 0

    Input = int(input("Please enter an integer that's not 0: "))

    while Input == 0:
        Input = int(input("Please enter an integer that's NOT 0: "))

    Largest = Input
    Smallest = Input
    Sum = Input

    Input = int(input("Please enter another integer, or enter 0 to stop: "))

    while Input != 0:
        Count = Count + 1
        Sum = Sum + Input
        if Input >= Largest:
            Largest = Input
        elif Input <= Smallest:
            Smallest = Input
        Input = int(input("Please enter another integer, or enter 0 to stop: "))

    print()
    print("The largest number is",Largest)
    print("The Smallest number is",Smallest)
    print("The average is",Sum / Count)
    print()
    strStart = input("Enter 'Y' to start again ")
    print()
