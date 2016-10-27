# Author: Jackie Xu
# Date: 9/29/2014
# Purpose: Explore more nested structures
#-------------------------------------------------------------------------------
import math

print("Welcome to the automated Parking Garage")
print()
Start = "Y"
while Start == "Y":
    TimeEnter = int(input("What time did you enter?(HHMM): "))

    while TimeEnter < 0 or TimeEnter >= 2400 or TimeEnter % 100 >= 60:
        TimeEnter = int(input("Please enter a VALID Time(HHMM): "))
    
    if TimeEnter >= 1800:
        print("Price: $5.00")
        print()
    else:
        Pass = input("Do you have a pass?(Y/N):")

        while not(Pass == "Y" or Pass == "N"):
            Pass = input("DO YOU HAVE A PASS?(Y/N):")

        Minutes = int(input("How many minutes are you planning to stay? "))
        while Minutes < 1 or Minutes > 1440:
            Minutes = int(input("please input a VALID number: "))

        Price = 3 * math.floor(0.05 * (Minutes - 1)) + 3

        TimeLeave = ((TimeEnter // 100) * 60 + TimeEnter % 100 + Minutes) // 60 * 100 + \
        ((TimeEnter // 100) * 60 + TimeEnter % 100 + Minutes) % 60

        NewTimeEnter = TimeEnter // 100 * 60 + TimeEnter % 100
             
        if TimeLeave >= 1800:
            Price = 3 * math.floor(0.05 * (1080 - NewTimeEnter) - 1) + 3
            if Price == 0:
                Price = Price + 3
                Price = Price + 5
        if Price >= 28:
                Price = 28

        if Pass == "Y":
            if Price >= 8.5:
                Price = 8.5
                    
        print("Price:","$%-0.2f"%Price)
        print()
    Start = input("Start again? (Y/N) ")
    print()
    
