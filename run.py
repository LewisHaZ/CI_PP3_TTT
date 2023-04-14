# Tic Tac Toe game
# We want to have game board, and to display it
# Something to handle play game
# Something to handle the turns
# Function to check for win or tie
# Function to switch the turn from x to o
import sys
import random
import time
import os
from colors import Color as Col
import validation as val


def logo():
    """ 
    Displays game name
    """
    print(Col.YELLOW + "Welcome to:")
    print(" ")
    print(Col.LOGO_B + "  _____ _        _____            _____            ")
    print(Col.LOGO_R + "  |_   _(_)      |_   _|          |_   _|          ")
    print(Col.LOGO_B + "    | |  _  ___    | | __ _  ___    | | ___   ___  ")
    print(Col.LOGO_R + "    | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ ")
    print(Col.LOGO_B + "    | | | | (__    | | (_| | (__    | | (_) |  __/ ")
    print(Col.LOGO_R + "    \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___| ")
    print(Col.LOGO_B + "                                                   ")
    print(Col.LOGO_R + "                                                   ")
    print(Col.LOGO_B + "     __   __  _   _____   _  __   __               ")
    print(Col.LOGO_R + "     \ \ / / | | |  _  | | | \ \ / /               ")
    print(Col.LOGO_B + "      \ V /  | | | | | | | |  \ V /                ")
    print(Col.LOGO_R + "      /   \  | | | | | | | |  /   \                ")
    print(Col.LOGO_B + "     / /^\ \ | | \ \_/ / | | / /^\ \               ")
    print(Col.LOGO_R + "     \/   \/ | |  \___/  | | \/   \/               ")
    print(Col.LOGO_B + "             |_|         |_|                       ")
    print(" ")
    print(" ")
    print(Col.YELLOW + "                    a 2 player game.")
    separate_line()
    time.sleep(1)


def cls():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")


def separate_line():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print("- "*30)
    print(" ")


def main_menu() -> str:
    """
    This function will appear below the logo for the game,
    The user can select to view the rules or to start game.
    """
    time.sleep(1)
    print(Col.YELLOW + "Please select from the following: ")
    menu_options = "1. Game rules\n2. Start game\n"
    menu_option_selected = input(menu_options)
    separate_line()

    # Validate the input
    while menu_option_selected not in ("1", "2"):
        print(Col.YELLOW + "Please select from 1 or 2: ")
        menu_option_selected = input(menu_options)
        separate_line()

    if menu_option_selected == "1":
        cls()
        logo()
        rules()

    elif menu_option_selected == "2":
        start_game()

    return menu_option_selected


def rules():
    """
    Displays to the player the rules for Tic Tac Toe,
    they can exit this menu with any key
    """
    print(Col.YELLOW + "Game Rules are as follows: ")
    time.sleep(1)
    print("The goal of tic-tac-toe is to be the first player to get three" +
          "in a row on a 3-by-3 grid")
    time.sleep(1)
    print("This can be in a row, in a column or in a diagonal")
    time.sleep(1)
    print("Be careful though, you need to stop your opponent from doing" +
          "the same")
    time.sleep(1)
    print(Col.BLUE + "Tic Tac Toe is simple game of " +
                     "strategy and forward thinking.")
    time.sleep(1.5)
    print(" ")
    print(Col.YELLOW + "So good luck and have fun!")
    print(" ")
    time.sleep(1)
    separate_line()
    input("Enter any key to exit...\n")
    cls()
    main()


def start_game() -> str:
    """
    The function checks to see if it's the players first time
    """
    time.sleep(1)
    separate_line()
    print(Col.YELLOW + "Is this your first time playing?")
    answer = "1. Yes\n 2. No\n"
    answered = input(answer)
    separate_line()

    # Validate if answered with 1 or 2
    while answered not in ("1", "y", "2", "n"):
        print(Col.RED + "Please select from 1 or 2: ")
        answered = input(answer)

        separate_line()
       
    if answered == "1" or answered == "y":
        cls()
        logo()
        val.existing_acc(val.players)
     
    elif answered == "2" or answered == "n":
        cls()
        logo()
        val.register_new_players(val.players)
        
    return answered


BOARD_WIDTH = 3
BOARD_HEIGHT = 3

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# Who has won?
WINNER = None

# Whose turn is it?
CURRENT_PLAYER = 'X'

# Game running?
GAME_ACTIVE = True


class Board():
    def __init__(self):
        self.board = [[' ' for x in range(BOARD_WIDTH)]
                        for y in range(BOARD_HEIGHT)]
        self.moves = random.randint(0, 1)  # Random player starts the game

    def display_board(self):
        """
        Displays the game board of 3 columns and 3 rows.
        Dimensions declared in a variable
        """
        print(" ")
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])
    
    def whos_move(self) -> str:
        """
        Alternate moves between player 1 and 2
        """
        pieces = ['X', 'O']
        return pieces[self.moves % 2]
        
    def handle_turn(player):
        """
        A function to deal with the game
        delegating each player their turn
        and switching between.
        """
        print(player + "'s turn.")
        position = input("Choose a position from 1-9: ")

        valid = False

        while not valid:

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")

            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("That space is already filled, go again.")

        board[position] = player
        GAME_ACTIVE.display_board()
    
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
        check_win()
    
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
        global GAME_ACTIVE
        diag_1 = board[0] == board[4] == board[8] != "-"
        diag_2 = board[6] == board[4] == board[2] != "-"
    
        if diag_1 or diag_2:
            GAME_ACTIVE = False
        if diag_1:
            return board[0]
        elif diag_2:
            return board[6]
        return

    def check_if_tie():
        """
        A function to check if a player has tied
        the game: this will check rows, columns 
        and diagonals for the - symbol, if there
        is no - then the game is a tie.
        """
        global GAME_ACTIVE
        if "-" not in board:
            GAME_ACTIVE = False
        return
    
    def switch_player():
        """
        A function to switch from x's turn
        to o's turn and this repeats until
        a game state has been reached
        """
        global CURRENT_PLAYER
        if CURRENT_PLAYER == "X":
            CURRENT_PLAYER = "O"
        elif CURRENT_PLAYER == "O":
            CURRENT_PLAYER = "X"

        return

    def check_win():
        if row_wins or column_wins or diagonal_wins:
            cls()
            GAME_ACTIVE.display_board()
            if WINNER == Col.RED + 'X':
                print(Col.BLUE + "\n----> " +
                       f"{val.player1name.upper()}" + " is the winner <----\n")
                val.player1score += 1
                val.WORKSHEET.update_cell(val.player1email_row, 3, +
                                          val.player1score)
            
            else:
                print(Col.BLUE + "\n---->  " +
                       f"{val.player2name.upper()}" + " is the winner <----\n")
                val.player2score += 1
                val.WORKSHEET.update_cell(val.player2email_row, 3, +
                                            val.player2score)
            
            time.sleep(2)
            separate_line()
            play_again()
        
        return False


def run_game():
    """
    Runs through the logic for the game,
    displays the board and allows the game
    to start and finish.
    """
    GAME_ACTIVE.display_board()
    while GAME_ACTIVE:

        handle_turn(CURRENT_PLAYER)

        check_game_over()

        switch_player()

    if WINNER == 'X' or WINNER == 'O':
        print(WINNER + " WON.")
    elif WINNER is None:
        print("It's a tie.")


def play_again():
    """
    Give players an option to carry on playing with same players names
    go back to the main menu or exit the game
    """
    print(Col.GREEN + "What would you like to do:")
    options = "1) Play again\n2) Go to main menu\n\
3) See your statistics\n4) Quit game\n"
    selected = input(options)
    separate_line()

    # Validate if answer is either 1 or 2 or 3
    while selected not in ("1", "2", "3", "4"):
        print(Col.GREEN + "Please choose between one of below options:")
        selected = input(options)

        separate_line()

    if selected == "1":
        print(Col.BLUE + "Starting a new game for " +
              f"{val.player1name} & {val.player2name}!\n")
        time.sleep(2)
        run_game()

    elif selected == "2":
        time.sleep(1)
        cls()
        main()

    elif selected == "3":
        show_stats()
        time.sleep(1)
        play_again()

    elif selected == "4":
        print(Col.BLUE + "Thanks for playing! See you soon!\n")
        sys.exit()


def show_stats():
    """
    Display number of games won so far by each player
    who played in the last game
    """
    print(Col.BLUE + "Total number of games won by " +
          f"{val.player1name}: {val.player1score}")
    print(Col.BLUE + "Total number of games won by " +
          f"{val.player2name}: {val.player2score}")
    separate_line()


def main():
    """
    Run all program functions
    """
    logo()
    main_menu()


if __name__ == "__main__":
    main()