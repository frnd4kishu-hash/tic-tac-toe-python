# make the board set up
board = [ "1", "2", "3", 
         "4", "5", "6", 
         "7", "8", "9" 
         ]

print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])


# player 1 chooses their marker
player_1 = input("Player 1, choose your marker (X or O): ").upper()

if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"

#------------ Where the game starts (players choose positions)----------------------#
# player 1 chooses their position
position = int(input("Player 1, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_1

# print the board after player 1's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# player 2 chooses their position
position = int(input("Player 2, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_2

# print the board after player 2's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# player 1 chooses their position
position = int(input("Player 1, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_1

# print the board after player 1's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# player 2 chooses their position
position = int(input("Player 2, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_2

# print the board after player 2's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# player 1 chooses their position
position = int(input("Player 1, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_1

# print the board after player 1's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# player 2 chooses their position
position = int(input("Player 2, choose your position (1-9): "))

# place the marker on the board
board[position - 1] = player_2

# print the board after player 2's move
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])


#------------------------- Check for a winner -------------------------#
# check for player 1's win
if (board[0] == player_1 and board[1] == player_1 and board[2] == player_1) or \
   (board[3] == player_1 and board[4] == player_1 and board[5] == player_1) or \
   (board[6] == player_1 and board[7] == player_1 and board[8] == player_1) or \
   (board[0] == player_1 and board[3] == player_1 and board[6] == player_1) or \
   (board[1] == player_1 and board[4] == player_1 and board[7] == player_1) or \
   (board[2] == player_1 and board[5] == player_1 and board[8] == player_1) or \
   (board[0] == player_1 and board[4] == player_1 and board[8] == player_1) or \
   (board[2] == player_1 and board[4] == player_1 and board[6] == player_1):
    print("Player 1 wins!")


# check for player 2's win
if (board[0] == player_2 and board[1] == player_2 and board[2] == player_2) or \
   (board[3] == player_2 and board[4] == player_2 and board[5] == player_2) or \
   (board[6] == player_2 and board[7] == player_2 and board[8] == player_2) or \
   (board[0] == player_2 and board[3] == player_2 and board[6] == player_2) or \
   (board[1] == player_2 and board[4] == player_2 and board[7] == player_2) or \
   (board[2] == player_2 and board[5] == player_2 and board[8] == player_2) or \
   (board[0] == player_2 and board[4] == player_2 and board[8] == player_2) or \
   (board[2] == player_2 and board[4] == player_2 and board[6] == player_2):
    print("Player 2 wins!")


# check for a tie
if "-" not in board:
    print("It's a tie!")


# ------------------------- End of the game -------------------------#