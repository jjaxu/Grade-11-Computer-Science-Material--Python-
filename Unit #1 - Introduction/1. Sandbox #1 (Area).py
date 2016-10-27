# Author: Jackie Xu
# Purpose: Sandbox #1, Playing around with Python Syntax, calculate area of a triangle
# Date: 9/11/2014
#-------------------------------------------------------------------------------------
import math

sideA = float(input("Please enter a positive value (1st side): "))
sideB = float(input("Please enter a positive value (2nd side): "))
sideC = float(input("Please enter a positive value (3rd side): "))

while (sideA + sideB <= sideC or sideA + sideC <= sideB or sideB + sideC <= sideA):

    while sideA <= 0:
        sideA = int(input("Please re-enter a VALID POSITIVE value(1st side): "))

    while sideB <= 0:
        sideB = int(input("Please re-enter a VALID POSITIVE value (2nd side): "))

    while sideC <= 0:
        sideC = int(input("Please re-enter a VALID  POSITIVE value(3rd side): "))
        
    if sideA + sideB <= sideC or sideA + sideC <= sideB or sideB + sideC <= sideA:
        print("Invalid Values! Try again")
        sideA = float(input("Please enter a positive value (1st side): "))
        sideB = float(input("Please enter a positive value (2nd side): "))
        sideC = float(input("Please enter a positive value (3rd side): "))
    
semiP = 1.0/2*(sideA + sideB + sideC)

Area = math.sqrt(semiP*(semiP-sideA)*(semiP-sideB)*(semiP-sideC))

print("The Area of this triangle is", "%0.2f"%Area, "units squared.")

