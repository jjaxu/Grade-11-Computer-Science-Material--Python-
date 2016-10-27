# Author: Jackie Xu
# Date: 11/20/2014
# Purpose: Introduction to OOP, writing a calender program
# ==========================================================================

from tkinter import*
import datetime

now = datetime.datetime.now()

root = Tk(className = " Calender")
root.config(width = 800, height = 600)

day = StringVar()
month = StringVar()
year = StringVar()

day.set(value = "1")
month.set(value = "1")
year.set(value = "2000")
#-------------------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/6/2014
# Purpose: "Bob" check function
# Parameters: String input
# Return Value: True/False

def bobRangeCheck(strInput,low = "NA",high = "NA"):
    ok = False
    
    if strInput.isdigit():
        if low == "NA" and high == "NA":
            ok = True
        elif low == "NA":
            if int(strInput) <= high:
                ok = True
        elif high == "NA":
            if int(strInput) >= low:
                ok = True
        else:
            if int(strInput) >= low and int(strInput) <= high:
                ok = True
    return ok
# --------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/20/2014
# Purpose: Creates an object with its own properties and methods
# Parameters" None
# Return: day, month, year, monthname, maxday, dayname

class Date:
    # Data fields-----------
    def __init__(self,day,month,year):
        
        self.day = day
        self.month = month
        self.year = year

        if self.calcValid():
            self.day = int(self.day)
            self.month = int(self.month)
            self.year = int(self.year)
    # Methods---------------

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: Returns the appropriate monthname given month #
    # Parameters: Self
    # Return: monthname
    
    def returnMonthName(self):
        if self.month == 1:
            mName = "January"
        elif self.month == 2:
            mName = "February"
        elif self.month == 3:
            mName = "March"
        elif self.month == 4:
            mName = "April"
        elif self.month == 5:
            mName = "May"
        elif self.month == 6:
            mName = "June"
        elif self.month == 7:
            mName = "July"
        elif self.month == 8:
            mName = "August"
        elif self.month == 9:
            mName = "September"
        elif self.month == 10:
            mName = "October"
        elif self.month == 11:
            mName = "November"
        else:
            mName = "December"
        return(mName)
    
    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: Determines whether a year is leap
    # Parameters: Self
    # Return: True/False
    
    def returnLeapYear(self):
        leap = False
        if self.year % 100 == 0:
            if self.year % 400 == 0:
                leap = True
        elif self.year % 4 == 0:
            leap = True
        return leap

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: Returns the max days given month
    # Parameters: Self
    # Return: maxday

    def returnMaxDay(self):
        maxDay = 31
        if self.month == 2:
            if self.returnLeapYear():
                maxDay = 29
            else:
                maxDay = 28
        elif self.month == 4 or self.month == 9 or \
             self.month == 6 or self.month == 11:
            maxDay = 30
            
        return maxDay

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: a complicated formula that determines day number given month,day and year
    # Parameters: Self
    # Return: day number

    def calcZeller(self):
        m = self.month - 2
        y = self.year

        if m <= 0:
            m = m + 12
            y = y - 1
        p = y // 100
        r = y % 100
        return(self.day + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: Returns the appropriate dayname given zeller number (day number)
    # Parameters: Self
    # Return: dayname

    def returnDayName(self):
        dayName = ""
        if self.calcZeller() == 0:
            dayName = "Sunday"
        elif self.calcZeller() == 1:
            dayName = "Monday"
        elif self.calcZeller() == 2:
            dayName = "Tuesday"
        elif self.calcZeller() == 3:
            dayName = "Wednesday"
        elif self.calcZeller() == 4:
            dayName = "Thursday"
        elif self.calcZeller() == 5:
            dayName = "Friday"
        else:
            dayName = "Saturday"
        return dayName

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/20/2014
    # Purpose: Determines whether the day, month and year actually exists
    # Parameters: Self
    # Return: True/False
    
    def calcValid(self):
        valid = False

        if bobRangeCheck(str(self.day),1,self.returnMaxDay()) \
           and bobRangeCheck(str(self.month),1,12) \
           and bobRangeCheck(str(self.year),1600,"NA"):
            valid = True
        return valid

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/21/2014
    # Purpose: Gets date input from user and verifies it
    # Parameters: Self
    # Return: day, month, year

    def getDate(self):
        
        global intDay
        global intMonth
        global intYear

        if intDay.isdigit() and intMonth.isdigit() and intYear.isdigit():
            self.day = int(intDay)
            self.month = int(intMonth)
            self.year = int(intYear)

        if not self.calcValid():
            self.day = 1
            self.month = 1
            self.year = 2000
    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/21/2014
    # Purpose: Returns the final date product
    # Parameters: Self
    # Return: full date name
    
    def __str__(self):
        date = self.returnDayName() + ", " + str(self.day) + " " + \
               self.returnMonthName() + " " + str(self.year)
       
        return date
    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/21/2014
    # Purpose: Returns the final date product
    # Parameters: Self
    # Return: full date name

    def displayCalender(self):
        
        objCalender.create_text(10, 60, anchor = W, text = "Sun", font = ("Calibri","16"))
        objCalender.create_text(70, 60, anchor = W, text = "Mon", font = ("Calibri","16"))
        objCalender.create_text(130, 60, anchor = W, text = "Tue", font = ("Calibri","16"))
        objCalender.create_text(190, 60, anchor = W, text = "Wed", font = ("Calibri","16"))
        objCalender.create_text(250, 60, anchor = W, text = "Thu", font = ("Calibri","16"))
        objCalender.create_text(310, 60, anchor = W, text = "Fri", font = ("Calibri","16"))
        objCalender.create_text(370, 60, anchor = W, text = "Sat", font = ("Calibri","16"))

        objCalender.create_text(10,20,anchor = W, text = self.__str__(), font = ("Calibri","16"))

        count = 0
        x = 10
        y = 90

        tempDate = Date("1",str(self.month),str(self.year))

        x = tempDate.calcZeller() * 60 + 10
        for count in range(1,tempDate.returnMaxDay()+1):
            if count <= 9:
                objCalender.create_text(x, y, anchor = W, text = "  " + str(count), font = ("Calibri","16"))
            else:
                objCalender.create_text(x, y, anchor = W, text = count, font = ("Calibri","16"))

            if count == self.day:
                objCalender.create_oval(x - 10,y - 20,x + 30,y + 20, outline = "red",width = 3)

            x = x + 60

            if x > 370:
                x = 10
                y = y + 40

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/26/2014
    # Purpose: Returns the Day of Year
    # Parameters: Self
    # Return: -
    

    def dayOfYear(self):
        feb = 28
        if self.returnLeapYear():
            feb = 29
        
        if self.month == 1:
            dOy = self.day
        elif self.month == 2:
            dOy = self.day + 31
        elif self.month == 3:
            dOy = self.day + 31 + feb
        elif self.month == 4:
            dOy = self.day + 31 + feb + 31
        elif self.month == 5:
            dOy = self.day + 31 + feb + 31 + 30
        elif self.month == 6:
            dOy = self.day + 31 + feb + 31 + 30 + 31
        elif self.month == 7:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30
        elif self.month == 8:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30 + 31
        elif self.month == 9:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31
        elif self.month == 10:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30
        elif self.month == 11:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        else:
            dOy = self.day + 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        return dOy
            
#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/24/2014
# Purpose: Does all the calculations
# Parameters: -
# Return: -

def go(firstTime = True):
    global myDate
    global lblErrorBox

    lblErrorBox.place_forget()
    
    if firstTime == True:
        myDate = Date(day.get(), month.get(), year.get())
    elif firstTime == "Today":
        myDate = Date(now.day,now.month,now.year)

    if myDate.calcValid():
        objCalender.delete("all")
        myDate.displayCalender()
        cmdPrevCentury.place(x = 300, y = 450)
        cmdPrevDecade.place(x = 350, y = 450)
        cmdPrevYear.place(x = 400, y = 450)
        cmdPrevMonth.place(x = 450, y = 450)
        cmdNextMonth.place(x = 550, y = 450)
        cmdNextYear.place(x = 600, y = 450)
        cmdNextDecade.place(x = 650, y = 450)
        cmdNextCentury.place(x = 700, y = 450)
        lblErrorBox = Label(window,text = ("This is day "  + str(myDate.dayOfYear())) + " of the year.",\
                            font = ("Calibri","14","bold"))
        lblErrorBox.place(x = 20, y = 500)

        day.set(value = myDate.day)
        month.set(value = myDate.month)
        year.set(value = myDate.year)

    else:
        objCalender.delete("all")
        lblErrorBox = Label(window,text = "The calender for this date either does not exist or is no longer accurate, please enter a valid date.", \
                    font = ("Calibri","14","bold"))
        lblErrorBox.place(x = 20, y = 500)
        
        cmdPrevCentury.place_forget()
        cmdPrevDecade.place_forget()
        cmdPrevYear.place_forget()
        cmdPrevMonth.place_forget()
        cmdNextMonth.place_forget()
        cmdNextYear.place_forget()
        cmdNextDecade.place_forget()
        cmdNextCentury.place_forget()
        #print("ERROR")

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the previous century
# Parameters: -
# Return: -

def prevCentury():
    myDate.year = myDate.year - 100
    
    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the previous decade
# Parameters: -
# Return: -

def prevDecade():
    myDate.year = myDate.year - 10
    
    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)


#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the previous year
# Parameters: -
# Return: -

def prevYear():
    myDate.year = myDate.year - 1

    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the previous month
# Parameters: -
# Return: -

def prevMonth():
    myDate.month = myDate.month - 1

    if myDate.month == 0:
        myDate.month = 12
        myDate.year = myDate.year - 1
    
    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the instantaneous moment
# Parameters: -
# Return: -

def dateToday():
    go(firstTime = "Today")
    


#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the next month
# Parameters: -
# Return: -

def nextMonth():
    myDate.month = myDate.month + 1
        
    if myDate.month == 13:
        myDate.month = 1
        myDate.year = myDate.year + 1

    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the next year
# Parameters: -
# Return: -

def nextYear():
    myDate.year = myDate.year + 1
    
    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the next decade
# Parameters: -
# Return: -

def nextDecade():
    myDate.year = myDate.year + 10
    
    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)

#-----------------------------------------------------------------

# Author: Jackie Xu
# Date: 11/27/2014
# Purpose: Shows the calender for the next century
# Parameters: -
# Return: -

def nextCentury():
    myDate.year = myDate.year + 100

    if not myDate.calcValid():
        myDate.day = 1
        
    go(firstTime = False)
    
# Main =================================================================

#Menu--------
menubar = Menu(root)

startMenu = Menu(menubar,tearoff = 0)
startMenu.add_command(label = "Show Today", command = lambda:dateToday())

startMenu.add_separator()
startMenu.add_command(label = "Exit", command = lambda:root.destroy())

menubar.add_cascade(label = "Calender Options", menu = startMenu)
root.config(menu = menubar)
#-------------

window = Canvas(root,width = 800, height = 600,bg = "Pale Turquoise")
window.place(x = 0,y = 0)

objCalender = Canvas(window, width = 450, height = 300, bg = "bisque")
objCalender.place(x = 300, y = 120)

window.create_text(20,40,anchor = W, text = "Calender", font = ("Calibri","40","bold"))
window.create_text(25,90,anchor = W, text = "Please enter the day, month and year respectively:" , font = ("Calibri","16"))

window.create_text(25, 130, anchor = W, text = "Day: ", font = ("Calibri","20","bold"))
window.create_text(25, 180, anchor = W, text = "Month: ", font = ("Calibri","20","bold"))
window.create_text(25, 230, anchor = W, text = "Year: ", font = ("Calibri","20","bold"))


lblErrorBox = Label(window,text = "Welcome to Calender! Plese enter a valid date to start, or click 'Today' to view today's date.", \
                    font = ("Calibri","14","bold"))
lblErrorBox.place(x = 20, y = 500)

txtDay = Entry(window,textvariable = day, width = 6, font = ("Calibri","20","bold"))
txtDay.place(x = 120, y = 115)

txtDay = Entry(window,textvariable = month, width = 6, font = ("Calibri","20","bold"))
txtDay.place(x = 120, y = 165)

txtDay = Entry(window,textvariable = year, width = 6, font = ("Calibri","20","bold"))
txtDay.place(x = 120, y = 215)

# ------------------------------------------------------------------------------------------------------------------

cmdDisplay = Button(window, text = "Show Calender!", width = 16, font = ("Calibri","20","bold"),command = lambda: go())
cmdDisplay.place(x = 25, y= 270)

cmdPrevCentury = Button(window, text = "<<<<", width = 4, font = ("Calibri","12","bold"),command = lambda: prevCentury())
cmdPrevDecade = Button(window, text = "<<<", width = 4, font = ("Calibri","12","bold"),command = lambda: prevDecade())
cmdPrevYear = Button(window, text = "<<", width = 4, font = ("Calibri","12","bold"),command = lambda: prevYear())
cmdPrevMonth = Button(window, text = "<", width = 4, font = ("Calibri","12","bold"),command = lambda: prevMonth())
cmdDateToday = Button(window, text = "Today", width = 4, font = ("Calibri","11","bold"),command = lambda: dateToday())
cmdNextMonth = Button(window, text = ">", width = 4, font = ("Calibri","12","bold"),command = lambda: nextMonth())
cmdNextYear = Button(window, text = ">>", width = 4, font = ("Calibri","12","bold"),command = lambda: nextYear())
cmdNextDecade = Button(window, text = ">>>", width = 4, font = ("Calibri","12","bold"),command = lambda: nextDecade())
cmdNextCentury = Button(window, text = ">>>>", width = 4, font = ("Calibri","12","bold"),command = lambda: nextCentury())

cmdDateToday.place(x = 500, y = 450)

mainloop()
