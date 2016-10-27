#
#
#
#---------------------------------------------------------------------------
import random

class PlayerHand:
    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()
        self.card3 = Card()
        self.card4 = Card()
        self.card5 = Card()

    def __str__(self):
        return self.card1.__str__() + "  " +  self.card2.__str__()  + "  " +  self.card3.__str__() + "  " +  \
               self.card4.__str__()  + "  " +  self.card5.__str__()


class Card:
    def __init__(self):
        self.suit = random.randint(1,4)
        self.rank = random.randint(1,13)

    def displayCard(self):
        print(self.rank,self.suit)

    def __ge__(self,secondCard):
        answer = False
        if self.rank > secondCard.rank:
            answer = True
        return answer
        
        
    def __str__(self):
        if self.suit == 1:
            suit = "H"
        elif self.suit == 2:
            suit = "S"
        elif self.suit == 3:
            suit = "C"
        else:
            suit = "D"
        rank  = (str) (self.rank)
        return rank + suit

# Main=================================================
firstCard = Card()
secondCard = Card()
myFirstHand = PlayerHand()

print(firstCard)
print(secondCard)
print(myFirstHand)

if firstCard >= secondCard:
    print("My first Card was larger!")
