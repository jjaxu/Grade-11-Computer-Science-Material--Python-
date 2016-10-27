# Author: Jackie Xu
# Date: 9/11/2014
# Purpose: Explore Python's syntax, more loops and decisions
# ------------------------------------------------------------

# Factorial 20
print("Factorial 20!")
count = 0
Num = 1

while count != 20:
    Num = Num * (count + 1)
    count = count + 1

print(Num)
print("")
 
# Add/Substract reciprocal patterns (Pi generator?! Not so accurate :/)
print("Pi generator?")
count = 1
denom = 1
Ans = 0

while count != 1000001:
    Num = 1/denom
    if denom > 0:
        denom = -denom - 2
    else:
        denom = -denom + 2
    Ans = Ans + Num
    count = count + 1
    #print(Ans)
    
Ans = 4 * Ans
print(Ans)
print("")

# Adding reciprocal quadratic patterns, taking the limit? 0.5? 
print("Series of Reciprocal Quadratic patterns")
count = 1
Num = 3
Ans = 0

while count != 1000001:
    Ans = Ans + 1/Num
    Num = 4 * (count+1)**2 - 1
    count = count + 1
    #print(Ans)
    
print(Ans)


