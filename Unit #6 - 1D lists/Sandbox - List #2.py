class IntGroup:
    def __init__(self,userSize = 0):
        self.size = userSize
        self.intGroup = []

    def __str__(self):
        return str(self.intGroup) + "[Size: " + str(self.size) + "]"

    def initAsNum(self,userSize = 0):
        self.intGroup = []
        self.size = userSize
        for intCount in range(1,userSize + 1):
            self.intGroup.append(userSize)

myIntGroup = IntGroup()
myIntGroup.initAsNum(21)
print(myIntGroup)
