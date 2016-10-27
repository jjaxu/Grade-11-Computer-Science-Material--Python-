# Author: Jackie Xu
# Date: 9/11/2014
# Experimenting more operations with edit loops, also introduces else ifs
#---------------------------------------------------------------------------

UserMark = int(input("PLease enter a mark (0 to 100): "))

while UserMark < 0 or UserMark > 100 :
    print("Your mark is INVALD!")
    UserMark = int(input("PLease enter a VALID mark (0 to 100): "))

if UserMark >= 80:
    print("Level 4, Well done")

elif UserMark >= 70:
    print("Level 3, Good")

elif UserMark >= 60:
    print("Level 2, Not too bad")

elif UserMark >= 50:
    print("Level 1, Pass")

elif UserMark >= 40:
    print("Credit Recovery, Last chance")

else:
    print("Fail :(")
