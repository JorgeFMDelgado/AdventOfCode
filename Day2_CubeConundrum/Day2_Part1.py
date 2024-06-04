# Open the file with the puzzle input
f = open("PuzzleInput.txt","r")

def SplitVariousDelimiters(str,dels):
    # Function to split a string "str" by the delimiters "dels"
    # Input: string "str"
    #        list "dels"
    # Output: list "resSplit"

    # For loop to add a space " " before each delimiters in "dels"
    for d in dels:
        str = " ".join(str.split(d))
    
    # The usual split function only split a string by whitespace (\t,\r,\n,\f and spaces), hence the idea of adding a space to the delimiters
    resSplit = str.split()

    # The function will return a list due to the split
    return resSplit


# Delimiters for the split of each line
delimiters=[",",";",":"]

# Initializing the final answer
FinalSum = 0

# For loop to cycle through each line of the puzzle input
for line in f:

    # We split each line to obtain each word and number
    lineSplit = SplitVariousDelimiters(line,delimiters)

    # Extraction of the numbers and name of colours. We start at 2 (lineSplit[2:]) to ignore "Game ID:"
    numbers = [int(i) for i in lineSplit[2:] if i.isdigit()]
    colours = [i for i in lineSplit[2:] if i=='green' or i=='blue' or i=='red']

    # Indice to correspond the number with a colour
    indColours = 0
    
    # For loop to cycle through each number that appear in each line
    for n in numbers:

        # If the number is larger than 14, then the game is impossible since there are no more than 14 dices of one colour
        if n > 14:
            break
        # If the number is equal to 14, then the game is impossible if the corresponding colour is not blue
        elif n == 14 and colours[indColours] != "blue":
            break
        # If the number is equal to 13, then the game is only possible if the corresponding colour is red
        elif n == 13 and colours[indColours] == "red":
            break
        # All remaining combinations of numbers and colours are always possible.

        indColours += 1

    # The only possible games are the ones where the possible loop was not breaked, thus indColours will be the same as the lenght of the list of numbers (or colours)
    if indColours==len(numbers):
        FinalSum += int(lineSplit[1])

print(FinalSum)

# Close file
f.close()