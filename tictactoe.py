# make the board set up
board = [ "-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-" 
         ]

print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])


# player 1 chooses their marker
player_1 = input("Player 1, choose your marker (X or O): ")

if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"