# PyCharm IDE
# Lab Exercise 7: Tic Tac Toe In Python
"""
1. Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a pad,
so you get a 3x3 board representation.
The board will be represented as follows:
|---|---|---|
| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
|---|---|---|
| 7 | 8 | 9 |
|---|---|---|
"""
def display_board(board):
    """
    Description:    Takes in a board of type list as its parameter, and prints out the 3x3 representation of tic tac toe board.
    Arguments:
        board       List representing the tic tac toe board
    Returns:
        None
    """
    print("|---|---|---|") #creation of board
    print("| %s | %s | %s |"%( board[1], board[2], board[3] ))
    print("|---|---|---|")
    print("| %s | %s | %s |"%( board[4], board[5], board[6] ))
    print("|---|---|---|")
    print("| %s | %s | %s |"%( board[7], board[8], board[9] ))
    print("|---|---|---|")

"""d
2. Write a function that takes in a player input and assigns their token as
either 'X' or 'O'
"""
def player_token():
    token = ''
    while token != 'x' and token !='o':
        token = input('player 1 choose x or o: ') #choosing which token
    player1 = token
    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
    return (player1, player2)

"""
3. Write a function that takes in the board of type list, a token (either 'O' or 'X'), and a desired position (1-9)
as parameters, and assigns the token to the board.
"""
def place_token(board, token, pos):
    board[pos] = token #asign token to board[pos]

"""
4. Write a function that takes in the board of type list, and checks if someone has won.
"""
def check_win(board, token):
    return ((board[4] == board[5] == board[6] == token) or #check rows
    (board[1] == board[2] == board[3] == token) or
    (board[7] == board[8] == board[9] == token) or
    (board[7] == board[4] == board[1] == token) or #check columns
    (board[8] == board[5] == board[2] == token) or
    (board[9] == board[6] == board[3] == token) or
    (board[1] == board[5] == board[9] == token) or #check diagonals
    (board[3] == board[5] == board[7] == token))

"""
5. Write a function that uses the module `random` to randomly decide which player goes first.
"""
import random #randomly select who is first by importing random
def first_turn():
    flip = random.randint(0,1) #random
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

"""
6. Write a boolean function that returns a boolean indicating if the board is full and returns a boolean value.
True if full, False otherwise.
"""
def is_full(board):
    for i in range(1,10):
        if is_free(board, i):
            return False #not full
    return True #board is full

"""
7. Write a function that checks if the specific location on board is freely available. 
|---|---|---|
| X | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
|---|---|---|
| 7 | 8 | 9 |
|---|---|---|
For example, checking position 1 returns False, while checking position 2 returns True
"""
def is_free(board, pos):
    return (board[pos] == '1' or #check if 1 ... 9 is available
    board[pos] == '2' or
    board[pos] == '3' or
    board[pos] == '4' or
    board[pos] == '5' or
    board[pos] == '6' or
    board[pos] == '7' or
    board[pos] == '8' or
    board[pos] == '9')

"""
8. Write a function that asks for a user's next move as positions 1-9 and then uses the
function from 7 to check if it is a free space. If it is, then return the position
for later use.
"""
def player_move(board):
    pos = 0            #see if conditions met or not, if not return pos if yes continue while loop
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_free(board, pos): 
        pos = int(input('Choose a position 1-9 '))
    
    return pos 

"""
9. Write a function that asks the player if they want to play again and returns True
if they do want to play again.
"""
def replay(): # we will ask if player wants to restart the game or not.
    return input('Play again? enter y or n ').startswith('y')

"""
10. Here comes the hard part! Use while loops and the functions you've made to run the game!
"""
def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        # Set the game up here (board, who first, choose tokens x, o)
        board = ['a', '1', '2', '3', '4', '5', '6', '7', '8', '9',] 
        player1_token, player2_token = player_token()
        
        turn = first_turn()
        print(turn + ' will go first')
        
        play_game = input('Ready to play? y or n ') #ask the player to play
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
        
    # Play the game 
        while game_on:
            if turn == 'Player 1': #Player 1 Turn
                
                display_board(board)#show the board
                pos = player_move(board)#choose position
                place_token(board, player1_token, pos)

                #check if won 
                if check_win(board, player1_token):
                    display_board(board)
                    print('Player 1 has won!!')
                    game_on = False
                #check if its a tie
                else:
                    if is_full(board):
                        display_board(board)
                        print('tie game')
                        break
                    else:
                        turn = 'Player 2' # if no tie and no win then next player turn
            else:
                #show the board  # Player2's turn.
                display_board(board)
                pos = player_move(board)
                place_token(board, player2_token, pos)
                
                #check if won 
                if check_win(board, player2_token):
                    display_board(board)
                    print('Player 2 has won!!')
                    game_on = False
                #check if its a tie
                else:
                    if is_full(board):
                        display_board(board)
                        print('tie game')
                        break
                    else:
                        turn = 'Player 1' #if no tie and no win then next player turn

    #if not replay():
        if not replay():
            break

if __name__ == "__main__":
    main()