# Author: Jackie Xu
# Date: 11/6/2014
# Purpose: Creating a GUI for Red Dog
# =============================================================================

from tkinter import*
import random
import time

root = Tk(className = " GUI - Red Dog")

# Declare
bet = StringVar()
totalBet = StringVar()
purse = IntVar()
purseLabel = StringVar()
status = StringVar()

card1 = StringVar()
card2 = StringVar()
card3 = StringVar()

cardType = StringVar()

# Init'
Test = False
intPurse = 100
invalid = "Invalid input! You either did not enter a number or your bet is out of range!"

bet.set(value = "0")
totalBet.set(value = "0")
purse.set(value = 100)
status.set(value = "")

card1.set("0")
card2.set("0")
card3.set("0")

cardType.set("null")
purseLabel.set("You have: $100")

# Functions-----------------------------------------------------------

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
# Date: 10/10/2014
# Purpose: prints the face of the card
# Parameters: card value 
# Return: card face

def getFace(Number):
    if Number == 14:
        card =  "Ace"
    elif Number == 11:
        card = "Jack"
    elif Number == 12:
        card = "Queen"
    elif Number == 13:
        card = "King"
    else:
        card = str(Number)
    return card
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
        ok = True
    else:
        ok = False
    return ok

# Author: Jackie Xu
# Date: 11/6/2014
# Purpose: "Bob" check function
# Parameters: String input
# Return Value: True/False

def bobRangeCheck(strInput,low = 0,high = 100):
    ok = False
    if strInput.isdigit():
        if int(strInput) >= low and int(strInput) <= high:
            ok = True
    return ok

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/11/2014
# Purpose: outputs card 3 when needed
# Parameters: -
# Return: -

def draw3rd():

    global Test
    global intCard3
    global myHand
    global intPurse

    cmdDraw3.grid_remove()
    cmdPlay.grid(row = 2, column = 0,sticky= W,padx = 10, pady = 5)

    txtBet.grid_remove()
    
    if Test == False:
        intCard3 = getCard()

    card3.set(value = "Card 3: " + getFace(intCard3))
    lblCard3.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 5)
    deal(intCard3,3,5,5)
    
    if handType(myHand) == "Pair":
        if intCard3 == myHand.card1:
            intPurse = intPurse + 11 * bet1
            status.set(value = "Jackpot! Your 3rd card matches your other cards, you win 11 times your bet!")
        else:
            status.set(value = "Your 3rd card does not match you other cards, it was a tie, no money lost.")
    else:
        bet.set(value = str(bet1 + bet2))

        if between(myHand,intCard3):
            status.set(value = "The 3rd card is between the first 2 cards! You Win " + str(payout(myHand)) + " times your total bet!")
            intPurse = intPurse + payout(myHand) * int(bet.get())
        else:
            status.set(value = "The 3rd card is not between the other cards, you lost $" + str(bet.get()))
            intPurse = intPurse - int(bet.get())
    
    purse.set(value = intPurse)
    purseLabel.set(value = "You have: $" + str(purse.get()))

    if intPurse <= 0:
        status.set(value = "Game Over! You have lost all your money. Better luck next time.")
    else:
        cmdRestart.grid(row = 6, column = 0,sticky= W,padx = 10, pady = 5)
    
    lblCard1.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
    lblCard2.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 5)
    lblHandType.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 5)
    lblPurse.grid(row = 0, column = 1, sticky = W, padx = 10, pady = 5)
    
    totalBet.set(value = "0")
    bet.set("")
    lblTotalBet.grid_remove()
    cmdPlay.grid_remove()
#-----------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/7/2014
# Purpose: calls other functions and give it to lambda
# Parameters: -
# Return: -

def play():
    
    global intPurse
    global Test
    global intCard3
    global myHand
    global bet1
    global betType

    intPurse = purse.get()
    bet1 = bet.get()
    
    if bobRangeCheck(bet1,1,intPurse):
        
        bet1 = int(bet.get())

        lblCard3.grid_remove()
        
        totalBet.set(value = "Total Bet: $" + str(bet1))
        lblTotalBet.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 5)

        
        if Test == False:
            myHand = getHand()

        card1.set(value = "Card 1: " + getFace(myHand.card1))
        card2.set(value = "Card 2: " + getFace(myHand.card2))
        
        deal(myHand.card1,1,5,5)
        deal(myHand.card2,2,5,5)

        cardType.set(value = handType(myHand))

        if handType(myHand) == "Pair":
            status.set(value = "You've got a pair, click the button to draw a 3rd card.")
            cmdDraw3.grid(row = 2, column = 1,sticky= W,padx = 10, pady = 5)
            cmdPlay.grid_remove()
            txtBet.grid_remove()
                
        elif handType(myHand) == "Consecutive":
            totalBet.set(value = "0")
            lblTotalBet.grid_remove()
            status.set(value = "These cards are consecutive, it's a tie, no money lost.")
            cmdRestart.grid(row = 6, column = 1,sticky= W,padx = 10, pady = 5)
            txtBet.grid_remove()
            cmdPlay.grid_remove()

        else:
            if intPurse - bet1 < bet1:
                status.set(value = "These cards are neither a pair nor consecutive, please make an addition bet between $0 and $" + str(intPurse - bet1))
                betType = 1
            else:
                status.set(value = "These cards are neither a pair nor consecutive, please make an addition bet between $0 and $" + str(bet1))
                betType = 2
                
            cmdBet2.grid(row = 2, column = 1,sticky= W,padx = 10, pady = 5)
            cmdPlay.grid_remove()

        lblCard1.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
        lblCard2.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 5)
        lblHandType.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 5,columnspan = 2)
        lblPurse.grid(row = 0, column = 1, sticky = W, padx = 10, pady = 5)
    else:
        status.set(value = invalid + " Please place a bet between $1 and $" + str(intPurse) + "!")

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/11/2014
# Purpose: deal with the second bet
# Parameters: -
# Return: -

def play2():

    global Test
    global intCard3
    global myHand
    global bet1
    global bet2
    global betType
    good = False
    
    bet2 = bet.get()

    if bet2.isdigit():
        if betType == 1:
            if bobRangeCheck(bet2,high = intPurse - bet1):
                good = True
        else:
            if bobRangeCheck(bet2,high = bet1):
                good = True
        
    if good:  
        bet2 = int(bet.get())
        totalBet.set(value = "Total Bet: $" + str(bet1 + bet2))
        lblTotalBet.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 5)
        status.set(value = "Now, click to draw the 3rd card")

        cmdBet2.grid_remove()
        cmdDraw3.grid(row = 2, column = 1,sticky= W,padx = 10, pady = 5)
        txtBet.grid_remove()
    else:
        if betType == 1:
            status.set(value = invalid + " Please make an addition bet between $0 and $" + str(intPurse - bet1) + "!")
        else:
            status.set(value = invalid + " Please make an addition bet between $0 and $" + str(bet1) + "!")
        
#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/13/2014
# Purpose: Test mode allowing us to get any cards we want
# Parameters: -
# Return: -

def test():
    global Test
    global intCard3
    global myHand
    
    Test = True
    myHand.card1 = int(input("card1: "))
    myHand.card2 = int(input("card2: "))
    intCard3 = int(input("card3: "))

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/13/2014
# Purpose: Resets game when the player wins/loses
# Parameters: -
# Return: -

def reset():
    cmdRestart.grid_remove()
    lblCard1.grid_remove()
    lblCard2.grid_remove()
    lblCard3.grid_remove()
    
    cmdPlay.grid(row = 2, column = 0,sticky= W,padx = 10, pady = 5)
    status.set(value = "Please place a bet between $1 and $" + str(intPurse))
    
    txtBet.grid(row = 1, column = 1,sticky= W,padx = 10, pady = 5)

    canvas1.delete("all")
    canvas2.delete("all")
    canvas3.delete("all")

#--------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/18/2014
# Purpose: deals the cards
# Parameters: -
# Return: -

def deal(myCard,canvasNum = 1, x = 5,y = 5):

    global picture1
    global picture2
    global picture3
    
    global canvas1
    global canvas2
    global canvas3

    face = myCard
    if face == 14:
        face = 1
        
    s = random.randint(1,4)
    if s == 1:
       suit = "h"
    elif s == 2:
       suit = "c"
    elif s == 3:
       suit = "d"
    else:
       suit = "s"
       
    if face == 1:
       n = "a" 
    elif face == 10:
       n = "t" 
    elif face == 11:
       n = "j" 
    elif face == 12:
       n = "q" 
    elif face == 13:
       n = "k"
    else:
       n = str(face)

    if canvasNum == 1:
        picture1 = PhotoImage (file = n + str(suit) + ".gif")
        canvas1.create_image(x,y,image=picture1,anchor=NW)
    if canvasNum == 2:
        picture2 = PhotoImage (file = n + str(suit) + ".gif")
        canvas2.create_image(x,y,image=picture2,anchor=NW)
    if canvasNum == 3:
        picture3 = PhotoImage (file = n + str(suit) + ".gif")
        canvas3.create_image(x,y,image=picture3,anchor=NW)
    
# Main ======================================================================

#Menu--------
menubar = Menu(root)

startMenu = Menu(menubar,tearoff = 0)
startMenu.add_command(label = "TEST MODE", command = lambda:test())

startMenu.add_separator()
startMenu.add_command(label = "Exit", command = lambda:root.destroy())

menubar.add_cascade(label = "Game", menu = startMenu)
root.config(menu = menubar)
#-------------

frmEmpty = Frame(root,width = 400, height = 200)
frmEmpty.grid(row = 7, column = 0, rowspan = 2, columnspan = 2, sticky = W, padx = 10, pady = 10)

canvas1 = Canvas(root, width = 80, height = 104,bg = "green")
canvas1.place(x = 15, y = 230)

canvas2 = Canvas(root, width = 80, height = 104, bg = "green")
canvas2.place(x = 115, y = 230)

canvas3 = Canvas(root, width = 80, height = 104, bg = "red")
canvas3.place(x = 255, y = 230)

status.set(value = "Welcome to Red Dog! Please place a bet between $1 and $" + str(intPurse))
myHand = getHand()

intCard1 = myHand.card1
intCard2 = myHand.card2

card1.set(value = "Card 1: " + str(myHand.card1))
card2.set(value = "Card 2: " + str(myHand.card2))


Label(root,text = "Red Dog",font = ("Arial","18","bold")).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)
Label(root,text = "Bet ($): ").grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)

# Input
bet.set(value = "0")

txtBet = Entry(root, textvariable = bet)
txtBet.grid(row = 1, column = 1,sticky= W,padx = 10, pady = 5)

#Process
lblCard1 = Label(root, textvariable = card1)
lblCard2 = Label(root, textvariable = card2)
lblCard3 = Label(root, textvariable = card3)
                 
lblHandType = Label(root, textvariable = status)
lblHandType.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 5,columnspan = 2)

lblTotalBet = Label(root, textvariable = totalBet)

lblPurse = Label(root, textvariable = purseLabel)
lblPurse.grid(row = 0, column = 1, sticky = W, padx = 10, pady = 5)

#--------------------------------------------------------------

cmdPlay = Button(root,text = "I'm feeling lucky!", command = lambda:play())
cmdPlay.grid(row = 2, column = 0,sticky= W,padx = 10, pady = 5)
cmdDraw3 = Button(root,text = "Draw 3rd Card", command = lambda:draw3rd())
cmdBet2 = Button(root,text = "Place second bet", command = lambda: play2())

cmdRestart = Button(root,text = "Play again", command = lambda: reset())
root.mainloop()

