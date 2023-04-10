# Tic Tac Toe game
# We want to have game board, and to display it
# Something to handle play game
# Something to handle the turns
# Function to check for win or tie
# Function to switch the turn from x to o

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def display_board():
    """
    A function to print the lines for 
    the game board.
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    """
    Runs through the logic for the game,
    displays the board and allows the game
    to start.
    """
    display_board()

    handle_turn()


def handle_turn()
    """
    A function to deal with the game
    delegating each player their turn
    and switching between
    """
    position = input("Choose a position from 1-9: ")


play_game()
