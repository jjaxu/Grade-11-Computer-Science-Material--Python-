# Author: Jackie Xu
# Date: 10/2/2014
# Purpose: make a simulator of the game "Red Dog" with sub programs
#--------------------------------------------------------------------

import random

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: using functions with a container that holds 2 card values

class TwoCard:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/2/2014
# Purpose: Random card generator
# Parameters: None 
# Return:Number of a card (card)

def getCard():
    rndInt = random.randint(2,14)
    card = rndInt
    return card
#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: a function that returns 2 values using the TwoCard class
# Parameters: None 
# Return: hand (2 numbers)

def getHand():
    hand = TwoCard(getCard(),getCard())
    return hand

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: prints the hands
# Parameters:2 value class container 
# Return: 2 hand numbers

def printHand(twoCardObj):
    if twoCardObj.card1 >= 2 and twoCardObj.card1 < 11:
        card1 = str(twoCardObj.card1)
    else:
        if twoCardObj.card1 == 11:
            card1 = "Jack"
        elif twoCardObj.card1 == 12:
            card1 = "Queen"
        elif twoCardObj.card1 == 13:
            card1 = "King"
        elif twoCardObj.card1 == 14:
            card1 = "Ace"
        

    if twoCardObj.card2 >= 2 and twoCardObj.card2 < 11:
        card2 = str(twoCardObj.card2)
    else:
        if twoCardObj.card2 == 11:
            card2 = "Jack"
        elif twoCardObj.card2 == 12:
            card2 = "Queen"
        elif twoCardObj.card2 == 13:
            card2 = "King"
        elif twoCardObj.card2 == 14:
            card2 = "Ace"
    print("Card #1:",card1)
    print("Card #2:",card2)

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/10/2014
# Purpose: prints the face of the card
# Parameters: card value 
# Return: card face

def printCard3(Number):
    if Number == 14:
        card3 =  "Ace"
    elif Number == 11:
        card3 = "Jack"
    elif Number == 12:
        card3 = "Queen"
    elif Number == 13:
        card3 = "King"
    else:
        card3 = str(Number)
    print("Card #3:",card3)

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: checks the type of the hand
# Parameters: 2 integers
# Return: Pair, Consecutive, non-consecutive

def handType(twoCardObj):
    if twoCardObj.card1 == twoCardObj.card2:
        handType = "Pair"
    elif abs(twoCardObj.card1 - twoCardObj.card2) == 1:
        handType = "Consecutive"
    else:
        handType = "Non-consecutive"
    return handType

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: counts the spead between the cards
# Parameters: 2 object container
# Return: number of spead

def spread(twoCardObj):
    spread = 0
    for count in range(1,abs(twoCardObj.card1 - twoCardObj.card2)):
        spread = spread + 1
    return spread

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: calculates the payout
# Parameters: TwoCard object
# Return: payout (1-5)

def payout(twoCardObj):
    if spread(twoCardObj) == 1:
        payout = 5
    elif spread(twoCardObj) == 2:
        payout = 4
    elif spread(twoCardObj) == 3:
        payout = 2
    else:
        payout = 1
    return payout

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 10/6/2014
# Purpose: calculates the payout
# Parameters: TwoCard object
# Return: payout (1-5)

def between(twoCardObj,newCard):
    if twoCardObj.card1 > twoCardObj.card2:
        bigCard = twoCardObj.card1
        smallCard = twoCardObj.card2
    else:
        bigCard = twoCardObj.card2
        smallCard = twoCardObj.card1
        
    if newCard > smallCard and newCard < bigCard:
        return True
    else:
        return False
#--------------------------------------------------------------------
    
# Author: Jackie Xu
# Date: 9/30/2014
# Purpose: A function that gets user input in range of (low,high)
# Parameters: Range of valid inputs(Low,High)
# Return Value: Valid user integer
# I stole this from my Number Theory assignment and changed it a bit

def getPositiveInteger(Low = 0,High = 100,prompt = ""):
    blnOK = False
    strNum = ""
    strPrompt = prompt + "between $" + str(Low) +" and $" + str(High) + ": "

    while not strNum.isdigit() or not blnOK:

        strNum = input(strPrompt)
        if strNum.isdigit():
            intNum = int(strNum)
            if intNum <= High and intNum >= Low:
                blnOK = True
            else:
                print("Your number is out of range!")
                
        else:
            print("You did not enter a NUMBER!")
    return intNum




# Main --------------------------------------------------------------
strStart = input("Welcome to Red Dog, enter 'Y' to start normal game, 'TEST' to enter test mode ")
print()
purse = 100


while (strStart == "Y" or strStart == "y" or strStart == "TEST") and purse > 0:
    
    #TEST MODE------------------------------------------------
    if strStart == "TEST":
        print("TESTING MODE")
        print("----------------------------------------------------")
        print()

        bet = getPositiveInteger(1,purse,"Please place a bet ")
        
        myHand = TwoCard(int(input("Card #1 (2-14): ")),int(input("Card #2 (2-14): ")))
     # ------------------------------------------------   
    else:
        print("Normal game")
        print("----------------------------------------------------")
        bet = getPositiveInteger(1,purse,"Please place a bet ")
        print()
        input("Press 'Enter' to draw the first 2 cards ")
        myHand = getHand()
    printHand(myHand)
    print()

    #purse = purse - bet
    
    if handType(myHand) == "Pair":
        input("You got a Pair, press 'Enter' to draw the 3rd card ")
        print()
        
        #TEST MODE------------------------------------------------
        if strStart == "TEST":
            card3 = int(input("Card #3 (2-14): "))
        #------------------------------------------------

        else:
            card3 = getCard()
        printCard3(card3)
        print()

        if card3 == myHand.card1:
            purse = purse + bet * 11
            print("You Win! You have won 11 times your bet money!")
            print()
        else:
            print("It was a tie, no money lost")
            print()
                  
    elif handType(myHand) == "Consecutive":
        print("These cards are Consecutive")
        print("It was a tie, no money lost")
        print()
    else:
        print("The cards were neither a Pair nor Consecutive")
        print()

        if purse - bet < bet:
            newBet = getPositiveInteger(0,purse - bet,"Please place another bet: ")
        else:
            newBet = getPositiveInteger(0,bet,"Please place another bet: ")
        bet = bet + newBet
        input("Press 'Enter' to draw a 3rd card ")

        #TEST MODE------------------------------------------------
        if strStart == "TEST":
            card3 = int(input("Card #3: "))
        else:
            card3 = getCard()
        
        #------------------------------------------------
        printCard3(card3)
        print()

        if between(myHand,card3):
            print(card3,"is between",myHand.card1,"and",myHand.card2)
            print()
            print("You Win! You have won",payout(myHand),"times your new bet money!")
            print()
            purse = purse + bet * payout(myHand)
        else:
            print(card3,"is not between",myHand.card1,"and",myHand.card2)
            print()
            purse = purse - bet
            print("You lost")

    print("Your new balance is now $" + str(purse))
    print("----------------------------------------------------")
    print()

    if purse >= 1:
        strStart = input("Play again? 'Y' to play again, 'TEST' to continue testing ")
        print()
    else:
        print("Game Over, You have lost all your money. Better luck next time.")
print("----------------------------------------------------")
print("Have a nice day!")

 
