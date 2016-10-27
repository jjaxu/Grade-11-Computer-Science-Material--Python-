import random
from tkinter import*

# THIS SAMPLE CODE HAS NOT BEEN FULLY CODED/IMPLEMENTED.
# Some Classes are NOT fully developed.
# Some Subs are NOT fully developed.

# Card class
# Fields:
#   face: number 1...13 representing
#         A, 2, ..., 10, J, Q, K
#   suit: "h", "c", "d", "s"
#   picture: the picture of the card
# Methods:
#   deal: establishes the field values
#         (purely random: it may generate two of
#          the same card)
#   display: draws the picture of the card given
#            the location
#   value: returns the card's  value

class Card:

    # constructor
    # Parameter: none
    def __init__(self):
        self.face = 0
        self.suit = ""
        self.picture = 0

    # deal
    # Purpose: Sets the fields randomly.
    #          The picture is 73 x 97 pixels.
    # Paramters: None.
    def deal(self):
        self.face = random.randint(1,13)
        s = random.randint(1,4)
        if s == 1:
            self.suit = "h"
        elif s == 2:
            self.suit = "c"
        elif s == 3:
            self.suit = "d"
        else:
            self.suit = "s"
        if self.face == 1:
            n = "a" 
        elif self.face == 10:
            n = "t" 
        elif self.face == 11:
            n = "j" 
        elif self.face == 12:
            n = "q" 
        elif self.face == 13:
            n = "k"
        else:
            n = str(self.face) 
        self.picture = PhotoImage \
           (file = n + str(self.suit) + ".gif")


    # display
    # Purpose: Displays the card picture at the
    #          given location.
    # Paramters: canvas and location
    #          of the picture
    def display(self, c, x, y):
        c.create_image (x, y,
            image = self.picture, anchor = NW)

    # value
    # Purpose: Returns the value of the card
    # Paramters: none
    # Return Value: 10 if the card is 10,J,Q,K
    #               11 if the card is an Ace 
    #               number value for others
    def value(self):
        if self.face >= 10:
            return 10
        elif self.face == 1:
            return 11
        else:
            return self.face
        
    # overloaded str operator
    # Purpose: returns the card as a string
    # Parameters: None
    # Return value: eg. "7 of Clubs" or
    #                   "Queen of Hearts"
    def __str__(self):
        if self.face == 1:
            n = "Ace"
        elif self.face == 11:
            n = "Jack"
        elif self.face == 12:
            n = "Queen"
        elif self.face == 13:
            n = "King"
        else:
            n = str(self.face)
        if self.suit == "h":
            s = "Hearts"
        elif self.suit == "s":
            s = "Spades"
        elif self.suit == "d":
            s = "Diamonds"
        else:
            s = "Clubs"
        return n + " of " + s

class Deck:
    def __init__(self): 
        nothing = 0

class Hand:
    def __init__(self): 
        nothing = 0



cardTable = Tk()
cardTable.title ("Card Table")
cardTable.config(background = "white", width = 410, height = 500)
canvas = Canvas(cardTable, width = 400, height = 450)
canvas.config(background = "green")
canvas.place(x = 1, y = 40)

d = Deck()
game = []

def newDeck():
    nothing
    deald.config(state = NORMAL)

def display():    
    nothing
    deald.config(state = NORMAL)
            
def shuffle():
    nothing
    deald.config(state = NORMAL)

def deal():    
    nothing

    
newd = Button (cardTable, text ="New Deck    ", command = newDeck)
newd.place(x = 10,y = 5)
displayd = Button (cardTable, text ="Display Deck", command = display)
displayd.place(x = 120,y = 5)
shuffled = Button (cardTable, text ="Shuffle Deck", command = shuffle)
shuffled.place(x = 230,y = 5)
deald = Button (cardTable, text ="Deal Deck   ", command = deal, state = DISABLED)
deald.place(x = 340,y = 5)

cardTable.mainloop()
