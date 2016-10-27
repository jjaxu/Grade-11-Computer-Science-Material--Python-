# Author: Jackie Xu
# Date: 1/19/2015
# Purpose: To work with functions to strings and read/write to files
# ===================================================================


class JustifyText:
    
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: A class which will handle different parts of the text
    # Data fields -------
    #   wordsList: A list containing the individual words in the file
    #   docList: a list containing the lines of the justified text
    #   strInputFile: A string that holds the title of the inout file
    #   strJustification: A string that indicates the type of justification done
    #   intWidth: a value that contains the column width of the text
    # Methods ------
    #   __init__: contructor, creates the class with default parameters
    #   readFile: reads the file and put the words into a list
    #   writeFile: Writes the docList formatted that are defined in the parameters
    #   createDoc: Modifies docList depending on the field settings
    #   justifyLeft: Justify the text to the left side
    #   justifyRight: Justify the text to the right side by making changes to justifyLeft
    #   justifuCentre: Justify the text to centre by making slight changee to justifyLeft
    #   justifyFull: It makes every line in the text the same width, except the last line
    #   __str__: concatenates line from doc list, and returns the full justified string

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: Constructor for tbe IntGroup Class
    # Parameters: self,strInputFile, strOutputFile, strJustification, intWidth
    # Return: -

    def __init__(self, inputFile = "input.txt", outputFile = "output.txt", \
                 justification = "l", width = 60):
        self.wordsList = []
        self.docList = []
        self.input = inputFile
        self.output = outputFile
        self.justification = justification
        self.width = width

        self.readFile()
        self.createDoc()

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: reads input file and makes all words into a list
    # Parameters: self
    # Return: -

    def readFile(self):
        file = open(self.input,"r")
        for line in file:
            tempList = line.strip().split()
            for word in tempList:
                if len(word) > 30:
                    word = word[:30]
                self.wordsList.append(word)
        file.close()

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: creates left justified lines to doc list by using words from wordsList
    # Parameters: self
    # Return: -

    def justifyLeft(self):
        tempLine = ""
        self.docList = []
        length = len(self.wordsList)
        count = 0
                     
        for count in range(0,length):
            
            if len(tempLine) + len(self.wordsList[count]) + 1 <= self.width:
                tempLine = tempLine + str(self.wordsList[count]) + " "
            else:
                self.docList.append(tempLine)
                tempLine = ""
                tempLine = tempLine + str(self.wordsList[count]) + " "

        self.docList.append(tempLine)
            

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: creates right justified lines to doc list by using words from wordsList
    # Parameters: self
    # Return: -

    def justifyRight(self):
        self.justifyLeft()
        for count in range(0,len(self.docList)):
            self.docList[count] = (self.width - len(self.docList[count].strip())) * " " + self.docList[count]
            #print((self.width - len(self.docList[count])))



    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: creates centre justified lines to doc list by using words from wordsList
    # Parameters: self
    # Return: -

    def justifyCentre(self):
        self.justifyLeft()
        for count in range(0,len(self.docList)):
            totalSpace = (self.width - len(self.docList[count].strip()))
            frontSpace = totalSpace // 2
            backSpace = totalSpace - frontSpace

            self.docList[count] = frontSpace * " " + self.docList[count].strip() + backSpace * " "
            
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/21/2015
    # Purpose: creates full justified lines to doc list by using words from wordsList
    # Parameters: self
    # Return: -

    def justifyFull(self):
        
        self.justifyLeft()
        for count in range(0,len(self.docList)):
            pos = 0
            length = len(self.docList[count].strip())
            constant = 2
            if self.docList[count] != self.docList[-1]:            
                while length < self.width:
                    if pos < length:
                        pos = self.docList[count].index(" ",pos)
                        self.docList[count] = self.docList[count][:pos + 1] + " " + self.docList[count][pos + 1:]
                        pos = pos + constant
                        length = length + 1
                    elif len(self.docList[count].strip()) != self.width:
                        #print("Back to start")
                        pos = 0
                        length = length - 1
                        constant = constant + 1
                    else:
                        # sentinel that prevents infinite loop
                        length = self.width
        
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/20/2015
    # Purpose: Concatenates docList into a full string
    # Parameters: self
    # Return: -

    def __str__(self):
        final = ""
        for count in range(0,len(self.docList)):
            new = str(self.docList[count])
            final = final + new + "\n"
        return final

    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/21/2015
    # Purpose: Creates the docList respectively to its given type
    # Parameters: self
    # Return: -

    def createDoc(self):
        if self.justification == "l":
            self.justifyLeft()
        elif self.justification == "r":
            self.justifyRight()
        elif self.justification == "c":
            self.justifyCentre()
        elif self.justification == "f":
            self.justifyFull()
        else:
            print("Bad parameter, defaulted to 'left'")
            self.justifyLeft()
   
    #------------------------------------------------------
    # Author: Jackie Xu
    # Date: 1/21/2015
    # Purpose: writes the justified text to its output file
    # Parameters: self
    # Return: -

    def writeFile(self):
        out = open(self.output, "w")
        out.write(self.__str__())
        out.close()
        print("File Written to " + "'" + self.output + "'.")
        print()
    
##myFile = JustifyText)
##print(myFile)
##print()
##
##myFile = JustifyText(justification = "r")
##print(myFile)
##print()
##
##myFile = JustifyText(justification = "c")
##print(myFile)
##print()

myFile = JustifyText(justification = "f",width = 60)
myFile.writeFile()
print(myFile)
print()

##myFile.justifyLeft()
##print(myFile)
##print("wordslist")
##print(myFile.wordsList)
##
##
##print()
##myFile.justifyLeft()
##print(len(myFile.wordsList))
##print("DocList")
##print(myFile.docList)
##
##print()
##print("left")
##print(60 * "=")
##print(myFile)
##
##print()
##myFile.justifyRight()
##print("right")
##print(60 * "=")
##print(myFile)
##
##
##print()
##myFile.justifyCentre()
##print("centre")
##print(60 * "=")
##print(myFile)
##
##
##print()
##myFile.justifyFull()
##print("Full")
##print(60 * "=")
##print(myFile)
