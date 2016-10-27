#
#
#
#---------------------------------------------------------------------------
import random


class Card:
    def __init__(self):
        self.suit = random.randint(1,4)
        self.rank = random.randint(1,13)

    def displayCard(self):
        print(self.rank,self.suit)

##    def __ge__(self,secondCard):
##        answer = False
        def __str__
        
firstCard = Card()
secondCard = Card()

firstCard.displayCard()
secondCard.displayCard()

