# Tic Tac Toe game
# We want to have game board, and to display it
# Something to handle play game
# Something to handle the turns
# Function to check for win or tie
# Function to switch the turn from x to o

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# Is the Game running?
GAME_ACTIVE = True

# Who won? Or is it a tie?
WINNER = None

# Whose turn is it?
CURRENT_PLAYER = 'X'


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
    while GAME_ACTIVE:
        
        handle_turn(CURRENT_PLAYER)

        check_game_over()

        switch_player()


def handle_turn(player):
    """
    A function to deal with the game
    delegating each player their turn
    and switching between.
    """
    position = input("Choose a position from 1-9: ")
    
    position = int(position) - 1

    board[position] = "X"
    display_board()


def check_game_over():
    """
    A function to check if the game
    has finished and what the condition
    is for the game over state win or tie.
    """
    check_if_win()
    check_if_tie()


def check_if_win():
    """
    A function to check if a player has won
    the game: this will check rows, columns
    and diagonals for a win game state.
    """
    return


def check_if_tie():
    """
    A function to check if a player has tied
    the game: this will check rows, columns 
    and diagonals for a tie game state.
    """
    return


def switch_player():
    """
    A function to switch from x's turn
    to o's turn and this repeats until
    a game state has been reached
    """

    return


play_game()
