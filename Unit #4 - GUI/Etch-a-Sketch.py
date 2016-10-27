# Author: Jackie Xu
# Date: 10/14/2014
# Purpose: To make a graphical output with tkinter's canvas
#-------------------------------------------------------------------------------

from tkinter import *
import math

# Author: Jackie Xu
# Date: 10/14/2014
# Purpose: Class container that holds a point (x,y)
# Parameters: x,y coordinates
# Return: -

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Draws a line up
# Parameters: colour, length, thickness
# Return: -

def drawUp(length = 0, thickness = 5,colour = "black"):
    global cursorPoint
    canvas.create_line(cursorPoint.x,cursorPoint.y,cursorPoint.x,cursorPoint.y - length,fill = colour,width = thickness)
    cursorPoint.y = cursorPoint.y - length

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Draws a line Down
# Parameters: colour, length, thickness
# Return: -

def drawDown(length = 0, thickness = 5,colour = "black"):
    global cursorPoint
    canvas.create_line(cursorPoint.x,cursorPoint.y,cursorPoint.x,cursorPoint.y + length,fill = colour,width = thickness)
    cursorPoint.y = cursorPoint.y + length
#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Draws a line Right
# Parameters: colour, length, thickness
# Return: -

def drawRight(length = 0, thickness = 5,colour = "black"):
    global cursorPoint
    canvas.create_line(cursorPoint.x,cursorPoint.y,cursorPoint.x + length,cursorPoint.y,fill = colour,width = thickness)
    cursorPoint.x = cursorPoint.x + length

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Draws a line Left
# Parameters: colour, length, thickness
# Return: -
# this is so repetititve, should I be writing a subprogram to write these comments? ;)

def drawLeft(length = 0, thickness = 5,colour = "black"):
    global cursorPoint
    canvas.create_line(cursorPoint.x,cursorPoint.y,cursorPoint.x - length,cursorPoint.y,fill = colour,width = thickness)
    cursorPoint.x = cursorPoint.x - length

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Draws a Circle
# Parameters: diameter, thickness, coordinates of top left corner of circle(x and y), colour
# Return: -

def drawCircle(diameter = 1, thickness = 1, x = 100, y = 100,colour = "black"):
    canvas.create_oval(x,y,x + diameter,y + diameter,outline = colour, width = thickness)

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/15/2014
# Purpose: Set the current cursorpoint to where ever is needed
# Parameters: x coordinate, y coordinate
# Return: -

def setCursorPoint(x = 100, y = 100):
    global cursorPoint
    cursorPoint.x = x
    cursorPoint.y = y

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/20/2014
# Purpose: draws a diagonal line by calling the straight line functions
# Parameters: quadrant(direction), angle, lengh of line, thickness, colour
# Return: -

def drawDiagonal(quadrant = 4, angle = 45, length = 20, thickness = 5,colour = "black"):
    x = 1
    y = math.tan(math.radians(angle)) * x
    hypot = math.sqrt(x ** 2 + y ** 2)
    count = 0

    if quadrant == 1:
        while count < length:
            drawRight(colour = colour,length = x,thickness = thickness)
            drawUp(colour = colour,length = y,thickness = thickness)
            count = count + hypot

    elif quadrant == 2:
        while count < length:
            drawLeft(colour = colour,length = x,thickness = thickness)
            drawUp(colour = colour,length = y,thickness = thickness)
            count = count + hypot

    elif quadrant == 3:
        while count < length:
            drawLeft(colour = colour,length = x,thickness = thickness)
            drawDown(colour = colour,length = y,thickness = thickness)
            count = count + hypot

    else: 
        while count < length:
            drawRight(colour = colour,length = x,thickness = thickness)
            drawDown(colour = colour,length = y,thickness = thickness)
            count = count + hypot

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/20/2014
# Purpose: draws any parabolic function
# Parameters: x-coordinate of vertex, y-coordinate of vertex, vertical stretch factor, length on left side, length on right side, colour, thickness
# Return: -

def drawParabola(Vx = 500,Vy = 50,stretch = 1/100,heightL = 600, heightR = 600, colour = "black",thickness = 3):
    NewxL = 0
    NewxR = 0
    Newy = 0

    if stretch > 0:
        while Newy + Vy < heightL:
            NewxL = NewxL - 1
            Newy = stretch * NewxL ** 2
            drawCircle(thickness,thickness,NewxL + Vx,Newy + Vy,colour)

        NewxL = 0
        NewxR = 0
        Newy = 0

        while Newy + Vy < heightR:
            NewxR = NewxR + 1
            Newy = stretch * NewxR ** 2
            drawCircle(thickness,thickness,NewxR + Vx,Newy + Vy,colour)
            
    else:
        while Newy + Vy > Vy - heightL:
            NewxL = NewxL - 1
            Newy = stretch * NewxL ** 2
            drawCircle(thickness,thickness,NewxL + Vx,Newy + Vy,colour)

        NewxL = 0
        NewxR = 0
        Newy = 0

        while Newy + Vy > Vy - heightR:
            NewxR = NewxR + 1
            Newy = stretch * NewxR ** 2
            drawCircle(thickness,thickness,NewxR + Vx,Newy + Vy,colour)

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/28/2014
# Purpose: draws a sine graph to create a wave
# Parameters: starting coordinate x, starting coordinate y, amplitude, frequency, total length, colour, thickness
# Return: -

def drawWave(Vx = 500,Vy = 50,amp = 2,freq = 1,length = 600, colour = "black",thickness = 2):
    x = 0
    for count in range(0,length):
        y = amp * math.sin(freq * x)
        drawCircle(thickness,thickness,x + Vx,y + Vy,colour)
        x = x + 1

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/21/2014
# Purpose: draws an exponential growth curve
# Parameters: starting coordinate x, starting coordinate y, stretch factor, colour, thickness
# Return: -

def drawCurve(Vx = 500,Vy = 50,stretch = 1.1,height = 600,colour = "black",thickness = 3):
    NewxR = 0
    Newy = 0

    if stretch > 0:
        while Newy + Vy < height:
            NewxR = NewxR + 0.1
            Newy = stretch ** NewxR

            drawCircle(thickness,thickness,NewxR + Vx,Newy + Vy,colour)
    else:
        while Newy + Vy > Vy - height:
            NewxR = NewxR + 0.1
            Newy = -1 * abs(abs(stretch) ** NewxR)

            drawCircle(thickness,thickness,NewxR + Vx,Newy + Vy,colour)

#-------------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 10/27/2014
# Purpose: draws the building windows/doors
# Parameters: starting coordinate x, starting coordinate y, length, height, quadrant(direction), thickness
# Return: -

def drawWindow(Vx = 100, Vy = 100, xLen = 50, yLen = 50,quadrant = 1,thickness = 3):
    global cursorPoint
    setCursorPoint(Vx, Vy)
    if quadrant == 1:
        drawUp(yLen,thickness)
        drawDiagonal(1,45,xLen,thickness)
        drawDown(yLen,thickness)
        drawDiagonal(3,45,xLen,thickness)

    else:
        drawDown(yLen,thickness)
        drawDiagonal(4,45,xLen,thickness)
        drawUp(yLen,thickness)
        drawDiagonal(2,45,xLen,thickness)

# main---------------------------------------------------------------------------
root = Tk()
root.title("Etch-a-Sketch")
canvas = Canvas(root,width = 1000, height = 600)
canvas.config(background = "gray")
canvas.pack()

cursorPoint = Point(x = 20, y = 10)

# "By: Jackie Xu"
drawDown(20,4)
drawDiagonal(1,30,10,4)
drawDiagonal(2,30,10,4)
drawDiagonal(1,30,10,4)
drawDiagonal(2,30,10,4)

setCursorPoint(30,cursorPoint.y)

drawDiagonal(4,60,15,4)
drawDiagonal(1,60,15,4)
drawDiagonal(3,60,30,4)

setCursorPoint(60,15)
drawCircle(2,3,cursorPoint.x,cursorPoint.y)
drawCircle(2,3,cursorPoint.x,cursorPoint.y + 10)

setCursorPoint(80,10)
drawRight(30,5)

setCursorPoint(95,10)
drawDown(20)
drawDiagonal(2, 45,15,5)

setCursorPoint(110,10)

drawCircle(20,5,cursorPoint.x,cursorPoint.y)
setCursorPoint(130,20)
drawDown(15,5)

setCursorPoint(160,10)
drawLeft(20)
drawDown(20,5)
drawRight(20,5)

setCursorPoint(170,10)
drawDown(20)

setCursorPoint(170,20)
drawDiagonal(1,45,14)
setCursorPoint(170,20)
drawDiagonal(4,45,14)

setCursorPoint(190,10)
drawCircle(2,5,190,10)

setCursorPoint(190,20)
drawDown(10)

setCursorPoint(200,20)
drawRight(10)
drawUp(10)
drawLeft(10)
drawDown(20)
drawRight(10)

setCursorPoint(240,10)
drawDiagonal(4,60,23)
setCursorPoint(254,10)
drawDiagonal(3,60,23)

setCursorPoint(260,10)
drawDown(20)
drawRight(10)
drawUp(20)

#Road
setCursorPoint(413,317.16)
drawRight(209.93)

setCursorPoint(1000,317.16)
drawLeft(62)

setCursorPoint(200,600)
drawDiagonal(1,45,400)
setCursorPoint(800,600)
drawDiagonal(2,45,400)
setCursorPoint(cursorPoint.x-20,cursorPoint.y + 20)

for count in range(1,7):
    drawDown(35,5)
    setCursorPoint(cursorPoint.x,cursorPoint.y + 20)

#Left buildings
setCursorPoint(200,600)
drawUp(320)
drawDiagonal(3,45,282.84)

setCursorPoint(0,280)
drawRight(200)
drawUp(120)
drawLeft(140)
drawDown(120)

drawCurve(0,480,-1.0275,200,thickness = 2.2)

setCursorPoint(200,160)
drawDiagonal(2,60,140)
drawDiagonal(3,60,140)

setCursorPoint(200,160)
drawDiagonal(1,45,70)
drawDiagonal(2,30.98,139.38)

setCursorPoint(250,110)
drawDown(440,5)

setCursorPoint(250,350)
drawDiagonal(1,45,150)
drawDown(200)

drawCircle(80,5,90,180)
drawCircle(1,5,130,220)

setCursorPoint(130,220)
drawDiagonal(3,60,30,thickness = 3)

setCursorPoint(130,220)
drawDiagonal(1,30,20, thickness = 3)

setCursorPoint(357,290)
drawDiagonal(3,45,150)

setCursorPoint(357,243)
drawLeft(106.07)

setCursorPoint(357,243)
drawUp(80)

drawDiagonal(1,45,75.59)

drawDown(280)
setCursorPoint(411,109)
drawLeft(162)

setCursorPoint(357,163)
drawLeft(105)

setCursorPoint(260,464)
drawDiagonal(1,45,120,2)

setCursorPoint(260,484)
drawDiagonal(1,45,120,2)

setCursorPoint(260,504)
drawDiagonal(1,45,120,2)

setCursorPoint(260,524)
drawDiagonal(1,45,120,2)


#Right Buildings
setCursorPoint(800,600)
drawUp(120)
drawDiagonal(4,45,170)


setCursorPoint(800,480)
drawRight(200)
drawUp(100)
drawLeft(200)
drawDiagonal(2,45,150)
drawDown(220)

setCursorPoint(cursorPoint.x,cursorPoint.y - 220)
drawRight(200)
drawDiagonal(4,45,150)

setCursorPoint(800,480)
drawUp(100)
drawLeft(40,thickness = 3)
drawDown(100,thickness = 3)
drawRight(40,thickness = 3)


setCursorPoint(693,273)
drawUp(100)
drawDiagonal(2,45,100,colour = "gray")
drawDown(320)

drawCircle(142,5,622,31)

setCursorPoint(764,102)
drawDown(171)

setCursorPoint(743,493)
drawDown(50,2)

#ICS3U sign
setCursorPoint(270,370)
drawUp(30,thickness = 3)

setCursorPoint(285,327)
drawDiagonal(3,45,10,thickness = 3)
drawDown(25,thickness = 3)
drawDiagonal(1,45,10,thickness = 3)

setCursorPoint(290,350)
drawDiagonal(1,45,12.5,thickness = 3)
drawUp(12.5,thickness = 3)
drawDiagonal(3,45,12.5,thickness = 3)
drawUp(12.5,thickness = 3)
drawDiagonal(1,45,12.5,thickness = 3)

setCursorPoint(305,310)
drawDiagonal(1,45,12.5,thickness = 3)
drawDown(12.5,thickness = 3)
drawDiagonal(3,45,12.5,thickness = 3)

setCursorPoint(314,313.5)
drawDown(12.5,3)
drawDiagonal(3,45,12.5,thickness = 3)

setCursorPoint(320,295)
drawDown(25,3)
drawDiagonal(1,45,12.5,3)
drawUp(25,3)

#mountains
drawParabola(40,80,0.03,150,118)
drawParabola(300,40,0.005,82,200,"black")
drawParabola(Vx = 600, Vy = 60,stretch = 1/100, heightL = 310,heightR = 67)
drawParabola(Vx = 800, Vy = 100,stretch = 1/200, heightL = 107,heightR = 310)
drawParabola(Vx = 1000, Vy = 40,stretch = 1/50, heightL = 170,heightR = 0)

drawWave(525,120,5,0.1,98,"black",3)
drawWave(10,110,3,0.3,65,"black")
drawWave(620,100,15,0.04,140,"black")

#windows/doors
drawWindow(260,540,120,100)
drawWindow(375,425,30,40)

drawWindow(365,375,50,25)
drawWindow(365,335,50,25)
drawWindow(365,295,50,25)
drawWindow(365,255,50,25)
drawWindow(365,215,50,25)

drawWindow(640,390,50,50,2)
drawWindow(630,320,70,50,2)
drawWindow(630,250,70,50,2)
drawWindow(630,180,70,50,2)

drawWindow(725,475,50,50,2)
drawWindow(704,300,66,140,2)
drawWindow(100,700,100,100)
drawWindow(130,530)
drawWindow(60,590)

#12 / 10 shop sign
setCursorPoint(770,390)
drawDown(30,2)

setCursorPoint(790,420)
drawLeft(15,2)
drawUp(15,2)
drawRight(15,1)
drawUp(15,2)
drawLeft(15,2)

setCursorPoint(770,430)
drawRight(20,2)

setCursorPoint(770,440)
drawDown(30,2)

setCursorPoint(775,470)
drawUp(30,2)
drawRight(15,2)
drawDown(30,2)
drawLeft(15,2)

mainloop()
