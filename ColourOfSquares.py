#ColourOfSquares
position = input("Enter a position on the chess board: ")
column = position[0].lower()
row = int(position[1])
if column in "a,c,e,g":
    Black = True
else:
    Black = False
if Black:
    if row % 2 == 0:
        white = True
    else:
        white = False
else:
    if row % 2 == 0:
        white = False
    else:
        white = True
if white:
    print ("That position is white")
else:
    print("That position is black")