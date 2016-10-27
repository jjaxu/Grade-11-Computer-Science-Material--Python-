class TwoCard:
    def __init__(self,card1,card2):
        self.card1 = card1
        self.card2 = card2

def getCard():
    return 14

def getHand():
    return TwoCard(getCard(),getCard())





#Main
myHand = getHand()
print(myHand.card1,myHand.card2)
