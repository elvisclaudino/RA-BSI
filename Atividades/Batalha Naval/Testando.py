board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}

# We want 5 battleships, so we use a for loop to ask for a ship 5 times!
for n in range(5):
    print("Where do you want ship ", n + 1, "?")
    column = input("column (A to E):")
    row = input("row (1 to 5):")
    # columns are letters, so here we use the dictionary to get the number corresponding to the
    # letter
    column_number = letters_to_numbers[column]
    # The player enters numbers from 1 to 5, but we have to substract 1 to use python lists that
    # start on zero.
    row_number = int(row) - 1

    board[row_number][column_number] = 'X'

    # Show the board, one row at a time
    for row in board:
        print(row)

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")

    if column not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D or E")

    if row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")

# Now clear the screen, and the other player starts guessing
print("\n"*50)

# Keep playing until we have 5 right guesses
guesses = 0
while guesses < 5:
    print("Guess a battleship location")
    column = input("column (A to E):")

    if column not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D or E")

    row = input("row (1 to 5):")

    if row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")

    # columns are letters, so here we use the dictionary to get the number corresponding to the
    # letter
    column_number = letters_to_numbers[column]
    # The player enters numbers from 1 to 5, but we have to substract 1 to use python lists that
    # start on zero.
    row_number = int(row) - 1

    # Check if there was a hit or a miss
    if board[row_number][column_number] == 'X':
        print("HIT!")
        guesses = guesses + 1
    else:
        print("MISS!")

print("GAME OVER!")