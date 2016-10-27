# Author: Jackie Xu
# Date: 9/12/2014
# explore multi-way decisions
#-----------------------------
# Middle Number finder

Num1 = 0
Num2 = 0
Num3 = 0

Num1 = int(input("Please input your 1st number (Must be positive and even): "))
while Num1 < 0 or Num1 % 2 != 0:
    print("Your value is INVALD!")
    Num1 = int(input("Please put a POSITIVE EVEN number: "))

Num2 = int(input("Please input your 2nd number (Must be positive, even and different than the 1st: "))
while Num2 < 0 or Num2 % 2 != 0 or Num2 == Num1:
    print("Your value is INVALD!")
    Num2 = int(input("Please put a POSITIVE EVEN number that's different than the 1st: "))

Num3 = int(input("Please input your 3rd number (Must be positive, even, different than the 1st and the 2nd: "))
while Num3 < 0 or Num3 % 2 != 0 or Num3 == Num1 or Num3 == Num2:
    print("Your value is INVALD!")
    Num3 = int(input("Please put a POSITIVE EVEN number that's different than the 1st and 2nd: "))

if (Num1 > Num2 and Num1 < Num3) or (Num1 > Num3 and Num1 < Num2):
    print("The middle number is:",Num1)
elif (Num2 > Num1 and Num2 < Num3) or (Num2 > Num3 and Num2 < Num1):
    print("The middle number is:",Num2)
else:
    print("The middle number is:",Num3)
