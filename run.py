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
    to start and finish.
    """
    display_board()
    while GAME_ACTIVE:
        
        handle_turn(CURRENT_PLAYER)

        check_game_over()

        switch_player()


    if WINNER == 'X' or WINNER == 'O':
        print(WINNER + "WON.")
    elif WINNER == None:
        print("It's a tie.")



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
    global WINNER
    row_wins = check_rows()
    col_wins = check_columns()
    diag_wins = check_diagonals()
    if row_wins:
        WINNER = row_wins
    elif col_wins:
        WINNER = col_wins
    elif diag_wins:
        WINNER = diag_wins
    else:
        WINNER = None

    return


def check_rows():
    """
    Checking if any of the rows have the same
    value BUT not the initial dash placeholder.
    If the condition is met then it ends the 
    game.
    """
    global GAME_ACTIVE
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        GAME_ACTIVE = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    """
    Checking if any of the columns have the same
    value BUT not the initial dash placeholder.
    If the condition is met then it ends the 
    game.
    """
    global GAME_ACTIVE
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        GAME_ACTIVE = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    """
    Checking if any of the diagonals have the same
    value BUT not the initial dash placeholder.
    If the condition is met then it ends the 
    game.
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
