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


char = list(set(f.read()))
char.sort()

NoNumericalChar = [c for c in char if not c.isdecimal()]

print(NoNumericalChar)

f.seek(0)






# Close file
f.close()