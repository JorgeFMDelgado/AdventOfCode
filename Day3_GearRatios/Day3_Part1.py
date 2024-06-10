# Open the file with the puzzle input
f = open("PuzzleInput.txt","r")


matrix = [list(line.strip()) for line in f]



char = list(set(str(matrix)))
char.sort()



NoNumericalChar = [c for c in char if not c.isdecimal()]



for line in matrix:
    print([n for n in line if n.isdecimal()])
    break









# Close file
f.close()