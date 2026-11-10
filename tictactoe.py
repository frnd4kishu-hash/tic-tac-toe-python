#------------------------------ The Board Set up-------------------------------------#
board = [ "1", "2", "3", 
         "4", "5", "6", 
         "7", "8", "9" 
         ]

print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])


# player 1 chooses their marker

player_1 = input("Player 1, choose your marker (X or O): ").upper()
while player_1 != "X" and player_1 != "O":
    player_1 = input("Player 1, choose your marker (X or O): ").upper()

if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"

#------------ Where the game starts (players choose positions)----------------------#

current_player = player_1
player_number = 1
game_on = True
moves = 0
while game_on:
    position = input(f"Player {player_number}, choose your position (1-9): ")
    # reject anything that isn't a number from 1 to 9
    if not position.isdigit() or int(position) < 1 or int(position) > 9:
        print("Please type a number from 1 to 9.")
        continue

    position = int(position)

    # if the square is already taken, ask again
    if board[position - 1] == player_1 or board[position - 1] == player_2:
        print("That square is taken, pick another one.")
        continue

    board[position - 1] = current_player
    moves += 1
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    # check if the player who moved has won
    if (board[0] == current_player and board[1] == current_player and board[2] == current_player) or \
       (board[3] == current_player and board[4] == current_player and board[5] == current_player) or \
       (board[6] == current_player and board[7] == current_player and board[8] == current_player) or \
       (board[0] == current_player and board[3] == current_player and board[6] == current_player) or \
       (board[1] == current_player and board[4] == current_player and board[7] == current_player) or \
       (board[2] == current_player and board[5] == current_player and board[8] == current_player) or \
       (board[0] == current_player and board[4] == current_player and board[8] == current_player) or \
       (board[2] == current_player and board[4] == current_player and board[6] == current_player):
        print(f"Player {player_number} wins!")
        game_on = False

        # check for a tie

    if moves == 9 and game_on:
        print("It's a tie!")
        game_on = False

    # flip the turn
    if current_player == player_1:
        current_player = player_2
        player_number = 2
    else:
        current_player = player_1
        player_number = 1



# ----------------------------- End of the game ---------------------------------#