# PyCharm IDE
# import random
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
    print("|---|---|---|")
    print("| %s | %s | %s |"%( board[0], board[1], board[2] ))
    print("|---|---|---|")
    print("| %s | %s | %s |"%( board[3], board[4], board[5] ))
    print("|---|---|---|")
    print("| %s | %s | %s |"%( board[6], board[7], board[8] ))
    print("|---|---|---|")



"""
2. Write a function that takes in a player input and assigns their token as
either 'X' or 'O'
"""

def player_token():
    """
    Description:    Asks the Player 1 for input using input() and assign their token to either 'X' or 'O'
    Arguments:
        None
    Returns:
        marker      'tuple' object, e.g. ('X', 'O') means that Player 1 uses token 'X' and Player 2
                    uses 'O'
    """
    marker = None # set marker to None


    # while marker is not 'X' or 'O'
        # ask the user for input
        # if player selects 'X'
            # assign ('X', 'O') to marker
        # otherwise assign ('O', 'X')

    # return marker
    return marker


"""
3. Write a function that takes in the board of type list, a token (either 'O' or 'X'), and a desired position (1-9)
as parameters, and assigns the token to the board.

e.g.
place_token(board, 'X', 5)
board = ['1', '2', '3', '4', 'X', '6', '7', '8', '9']
|---|---|---|
| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
|---|---|---|
| 7 | 8 | 9 |
|---|---|---|
"""

def place_token(board, token, pos):
    """
    Description:    Updates the board by placing the token at the location 'pos' provided by the
                    player
    Arguments:
        board       List representing the tic tac toe board
        token       Token ('O' or 'X') of a player who makes a move
        pos         Position in tic tac toe (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Returns:
        board       'list' object representing the updated tic tac toe board

    """
    # locate the index of pos and assign it to variable pos_index
    # update the value of board[pos_index] with a token

    return board

"""
4. Write a function that takes in the board of type list, and checks if someone has won.
"""

def check_win(board, token):
    """
    Description:    Determines if the player has won
    Arguments:
        board       List representing the tic tac toe board
        token       Token ('O' or 'X') of a player who makes a move
    Returns:
                    'bool', True if the player who makes a move wins and False otherwise.
    """
    pass

"""
5. Write a function that uses the module `random` to randomly decide which player goes first.
"""

def first_turn():
    """
    Description:    Determines who makes the first turn
    Arguments:
        None
    Returns:
                    'str', Player who makes the first turn
    """

    # import random at the start of the script
    players = ['Player 1', 'Player 2']
    # using the method random.choice(), select the first player from the list players
    pass

"""
6. Write a function that returns a boolean indicating if the board is full.
True if full, False otherwise.
['1', '2', '3', '4', 'X', '6', '7', '8', '9'] => returns False
['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'] => returns True


"""

def is_full(board):
    """
    Description:    Determines if the board is full
    Arguments:
        None
    Returns:
                    'bool', True if the board is full, and False otherwise.
    """
    pass

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
    """
    Description:    Checks if the location 'pos' is free.
    Arguments:
        None
    Returns:
                    'bool', True if the location is free, and False otherwise.
    """
    # locate the index of pos and assign it to variable pos_index
    try:
        pos_index = board.index(pos)
    # if found, then it means the pos is not occupied
        return True
    # if not found, then the pos is occupied
    except ValueError: # handling ValueError in .index method
        # pos is not in list
        return False

"""
8. Write a function that asks for a user's next move as positions 1-9 and then uses the
function from 7 to check if it is a free space. If it is, then return the position
for later use.
"""
def player_move(board):
    """
    Description:    Asks the player for input (1-9) and uses is_free() function
                    to check if the position is free. If it is, then return the position
    Arguments:
        None
    Returns:
        position    'int', position provided by the user.
    """
    # input ("What is your next position? ")
    # if is_free(position) is true
    # return position
    pass

"""
9. Write a function that asks the player if they want to play again and returns True
if they do want to play again.
"""

def replay():
    pass

"""
10. Here comes the hard part! Use while loops and the functions you've made to run the game!
"""

def main():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Set the game up here
        # 1. setup an empty board
        # 2. Ask the player 1 for token (Valid choices are 'X' or 'O')
        # 3. Determine which player goes first using first_turn and assign it to a variable 'turn'

        play_game = input('Are you ready to play? Enter Yes or No. ')
        if play_game.lower()[0] == 'y':
            game_on = True
            print("Game started!")
        else:
            game_on = False
        # 4. provide the logic for player turns
        
        #while game_on:
        
            # Player 1 Turn.
            # 5. display board
            # 6. ask the user for move (using player_move)
            # 7. if free, place the token
            
            # 8. Check if player 1 has won using check_win()
            # 9. Else check if the board is full using is_full(board)
            # 10. Update the 'turn' variable to 'Player 2'

            # Player 2 Turn.

                #pass

        #if not replay():
            #break

if __name__ == "__main__":
    main()
