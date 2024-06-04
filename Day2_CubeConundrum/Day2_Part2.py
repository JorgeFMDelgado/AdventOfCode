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
FinalPower = 0

# For loop to cycle through each line of the puzzle input
for line in f:

    # We split each line to obtain each word and number
    lineSplit = SplitVariousDelimiters(line,delimiters)

    # Extraction of the numbers and name of colours. We start at 2 (lineSplit[2:]) to ignore "Game ID:"
    numbers = [int(i) for i in lineSplit[2:] if i.isdigit()]
    colours = [i for i in lineSplit[2:] if i=='green' or i=='blue' or i=='red']

    # We find the index on the list 'colours' of each individual colour
    # The function enumerate iterates through a list and outputs a tuple with the index and the quantity present in the list
    ind_colour_blue = [index for index,col in enumerate(colours) if col=='blue']
    ind_colour_green = [index for index,col in enumerate(colours) if col=='green']
    ind_colour_red = [index for index,col in enumerate(colours) if col=='red']

    # We find the corresponding number of dices for each colour and sort the new list in reverse to extract the highest number of dices, since it automatically tells us the minimum number of dices that we must have for the game to be possible
    n_blue_dices = [numbers[num] for num in ind_colour_blue]
    n_blue_dices.sort(reverse=True)

    n_green_dices = [numbers[num] for num in ind_colour_green]
    n_green_dices.sort(reverse=True)

    n_red_dices = [numbers[num] for num in ind_colour_red]
    n_red_dices.sort(reverse=True)

    # The power is computed by multiplying together the minimum numbers of dices of each colour
    power = n_blue_dices[0]*n_green_dices[0]*n_red_dices[0]

    FinalPower += power

print(FinalPower)

# Close file
f.close()