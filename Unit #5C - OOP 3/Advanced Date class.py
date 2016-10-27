# Author: Jackie Xu
# Date: 12/29/2014
# Purpose: To create an advanced date class with overloaded operations
#=====================================================================

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

#-------------------------------------------------------------------------
# Author: Jackie Xu
# Date: 11/20/2014
# Purpose: Creates an object with its own properties and methods
# Data fields: day, month and year
# Methods:
# returnMonthName: Returns the month name given it's month number
# returnLeapYear: Returns True if the its year is a leap year, otherwise False
# returnMaxDay: Returns the appropriate amount of days in a month
# calcZeller: A formula that can calculate the day number given a Date
# returnDayName: returns the corresponding day name using the Zeller number
# calcValid: checks if the Date is valid and actually exists
# getDate: Accepts inputs from the user to modify the Date, validation is done by calcValid
# __str__: converts the Date object into a string so that it can be printed
# dayOfYear: Returns the day of the year that the date is on
# __sub__: returns number of days between itself and another given date
# __gt__: retruns true if itself is greater than another given date, otherwise False
# __ge__: retruns true if itself is greater or equal to another given date, otherwise False
# __lt__: retruns true if itself is less than another given date, otherwise False
# __le__: retruns true if itself is less or equal to another given date, otherwise False
# __eq__: retruns true if itself is equal to another given date, otherwise False
# __ne__: retruns true if itself is NOT equal to another given date, otherwise False
# __add__: calculates the difference between to dates, then add the difference to the larger date, creating a new Date

class Date:
    # Data field-----------
    def __init__(self,day = 1,month = 1,year = 2000):
        
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
           and bobRangeCheck(str(self.year),1600,2400):
            valid = True
        return valid

    #-----------------------------------------------------------------

    # Author: Jackie Xu
    # Date: 11/21/2014
    # Purpose: Gets date input from user and verifies it
    # Parameters: Self
    # Return: day, month, year

    def getDate(self):

        intDay = input("Please enter the day: ")
        intMonth = input("PLease enter the month: ")
        intYear = input("Please enter the year (between 1600 and 2400): ")

        if intDay.isdigit() and intMonth.isdigit() and intYear.isdigit():
            self.day = int(intDay)
            self.month = int(intMonth)
            self.year = int(intYear)
        else:
            print("Invalid inputs! Valid NUMBERS only! Date has been defaulted to Saturday, 1 January 2000")
            self.day = 1
            self.month = 1
            self.year = 2000

        if not self.calcValid():
            print("Invalid Date! Date has been defaulted to Saturday, 1 January 2000")
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
    # Date: 12/29/2014
    # Purpose: Overloaded operator for subtracting 2 dates
    # Parameters: self, secondDate
    # Return: between

    def __sub__(self,secondDate):

        diff = 0
        
        big = Date(self.day,self.month,self.year)
        small = Date(secondDate.day,secondDate.month,secondDate.year)
        
        if self < secondDate:
            big = Date(secondDate.day,secondDate.month,secondDate.year)
            small = Date(self.day,self.month,self.year)


        while small != big:
            small.day = small.day + 1
            if small.day > small.returnMaxDay():
                small.day = 1
                small.month = small.month + 1
                if small.month > 12:
                    small.year = small.year + 1
                    small.month = 1
            diff = diff + 1
            
        return diff

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is greater than another
    # Parameters: self, secondDate
    # Return: True/False

    def __gt__(self,secondDate):
        greater = False
        if self.year > secondDate.year:
            greater = True
        elif self.year == secondDate.year:
            if self.month > secondDate.month:
                greater = True
            elif self.month == secondDate.month:
                if self.day > secondDate.day:
                    greater = True
        return greater
    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is greater or equal to another
    # Parameters: self, secondDate
    # Return: True/False

    def __ge__(self,secondDate):
        greaterEqual = False
        if self > secondDate or self == secondDate:
            greaterEqual = True
        return greaterEqual

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is less than another
    # Parameters: self, secondDate
    # Return: True/False

    def __lt__(self,secondDate):
        less = False
        if not self >= secondDate:
            less = True
        return less

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is less or equal to another
    # Parameters: self, secondDate
    # Return: True/False

    def __le__(self,secondDate):
        lessEqual = False
        if (not (self > secondDate)) or self == secondDate:
            lessEqual = True
        return lessEqual

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is equal to another
    # Parameters: self, secondDate
    # Return: True/False

    def __eq__(self,secondDate):
        equal = False
        if self.year == secondDate.year and \
           self.month == secondDate.month and \
           self.day == secondDate.day:
            equal = True
        return equal

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 12/29/2014
    # Purpose: Overloaded operator that checks whether if a date is not equal to another
    # Parameters: self, secondDate
    # Return: True/False

    def __ne__(self,secondDate):
        notEqual = False
        if not (self == secondDate):
            notEqual = True
        return notEqual

    #-----------------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/4/2015
    # Purpose: Overloaded operator that "adds" two dates
    # Parameters: self, secondDate
    # Return: newDate

    def __add__(self,secondDate):
        diff = self - secondDate
        if self > secondDate:
            newDate = Date(self.day,self.month,self.year)
        else:
            newDate = Date(secondDate.day,secondDate.month,secondDate.year)
            
        while diff != 0:
            newDate.day = newDate.day + 1
            if newDate.day > newDate.returnMaxDay():
                newDate.day = 1
                newDate.month = newDate.month + 1
                if newDate.month > 12:
                    newDate.year = newDate.year + 1
                    newDate.month = 1
            diff = diff - 1
        return newDate


    
# MAIN-------------------------------------------------------------------------------
date1 = Date()
date2 = Date()
print("Welcome to the calculator for two Dates! Please enter the following to start.")
print()

again = "Y"
while again == "Y" or again == "y":
    print("===========================================")
    print("Date #1")
    date1.getDate()
    print()

    print("Date #2")
    date2.getDate()
    print()

    print("The first date is: " + str(date1))
    print("The second date is " + str(date2))
    print()
    print("Are the dates Equal?: " + str(date1 == date2))
    print("Are they NOT Equal?: " + str(date1 != date2))
    print()
    print("Is the 1st Date greater than the 2nd?: " + str(date1 > date2))
    print("Is the 1st Date greater or equal to the 2nd: " + str(date1 >= date2))
    print()
    print("Is the 1st Date less than the 2nd: " + str(date1 < date2))
    print("Is the 1st Date less or equal to the 2nd: " + str(date1 <= date2))
    print()
    print("Difference between the two dates: " + str(date1 - date2) + " day(s)")
    print("Sum of the dates, created by adding the difference to the bigger date: " + str(date1 + date2))
    print()
    again = input("Would you like to enter another set of Dates? (Y/N): ")
    print()
print()
print("Have a nice day!")

