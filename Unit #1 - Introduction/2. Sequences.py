# Author: Jackie Xu
# Date: 9/11/2014
# Purpose: Experiment with Python's counting loops (Sequences)
#-------------------------------------------------------------

# Sequence 1
print ("Sequence #1 (Increasing Arithmetic Sequence) ")
Num = 2

while Num != 50:
    Num = Num + 3
    print(Num)
print (" ")


# Sequence 2
print ("Sequence #2 (Decreasing Arithmetic Sequence) ")
Num = 94

while Num != 50:
    Num = Num - 4
    print(Num)
print (" ")

# Sequence 3
print ("Sequence #3 (Increasing Geometric Sequence #1) ")
Num = 3

while Num != 49152:
    print(Num)
    Num = Num * 2
print (" ")

# Sequence 4
print ("Sequence #4 (Increasing Geometric Sequence #2) ")
count = 0
Num = 1

while count != 15:
    print(Num)
    Num = Num * 3
    count = count + 1
