# Open the file with the calibration info
f = open("CalibrationFile.txt","r")

CalNum = 0
for line in f:                          # for each line in the file f
    indNum = 0
    for char in line:                   # for each char in line
        if char.isdecimal():            # check if that char is a number
            if indNum == 0:             # if it is the first number, then save it
                FirstNum = int(char)

            LastNum = int(char)         # if there is more than one number, this quantity will always be replace by the following number
            indNum += 1
    
    LineNum = FirstNum*10 + LastNum     # Easy computation to have a 2 digit number with the first number as the decimal and the second number as the units
    CalNum += LineNum                   # Sum of all 2 digit numbers in each line

print(CalNum)

# Close the file
f.close()