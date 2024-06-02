# Open the file with the calibration info
f = open("CalibrationFile.txt","r")

# Convert all information into a list ordered by line
fList = f.readlines()
NumLines = len(fList)

# Dictionary to correspond each string to their respective number
DicNum = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

CalNum = 0

# For loop cycling through each line
for nline in range(NumLines):
    line = fList[nline]

    # Indicator to know if we already have the first decimal or text number
    indicatorNumOrText = 0

    # For loop cycling through each character
    for ind in range(len(line)):
    
        # Part associated to find the (possible) first and last decimal number
        char = line[ind]
        if char.isdecimal():
            if indicatorNumOrText == 0:
                FirstNum = int(char)
                indicatorNumOrText = 1
            LastNum = int(char)
            

        # Part associated to find the (possible) first and last text number
        Num3letter = line[ind:ind+3]    # Text number with 3 characters
        Num4letter = line[ind:ind+4]    # Text number with 4 characters
        Num5letter = line[ind:ind+5]    # Text number with 5 characters
       
        # For loop cycling through each key of the dictionary
        for StrNum in DicNum:
            # If a key is equal to a text number with 3, 4 or 5 letters
            if StrNum==Num3letter or StrNum==Num4letter or StrNum==Num5letter:
                if indicatorNumOrText == 0:
                    FirstNum = DicNum[StrNum]
                    indicatorNumOrText = 1
                LastNum = DicNum[StrNum]
    
    # Easy computation to have a 2 digit number with the first number as the decimal and the second number as the units
    LineNum = FirstNum*10 + LastNum     

    # Sum of all 2 digit numbers in each line
    CalNum += LineNum                   

print(CalNum)


# Close the file
f.close()