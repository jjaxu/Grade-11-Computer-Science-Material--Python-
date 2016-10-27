#  A new command to open a text file for reading.
# "R" means open file for read; "W" means open file for write.
file = open("testfile.txt", "r")
# each file or stream you wish to read/write to requires its own reference.
output = open("outputFile.txt", "w")
output2 = open("outputFile2.txt","w")

#  initializing an empty list
lstWords = []

#  in a loop; read a line from the file.
for line in file:
    # build a temporary 'list' of words from the current line
    # from the file, codes striped out; split by whitespace
    tempWordList = line.strip().split()
    # build the official list of words by apending words from the
    # temporary 'list' of words from the current line
    # truncating words exceeding 30 characters before adding them
    # to the official list of words.
    for strWord in tempWordList:
        if len(strWord) > 30:
            strWord = strWord[:30]
        lstWords.append(strWord)
        output2.write(strWord+" ")
# Print our the official list of words to check
print (lstWords)
output.write(str(lstWords))

# Make sure you close any file that you open.  forgetting to close a file
# opened for write will produce an empty file.
file.close()
output.close()
output2.close()
