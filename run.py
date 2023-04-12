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


class Board():
    def __init__(self):
        self.board = [[' ' for x in range(BOARD_WIDTH)]
                        for y in range(BOARD_HEIGHT)]
        self.moves = random.randint(0, 1) # Random player starts the game
        self.last_move = [-1, -1]

    def display_board(self):
        """
        Displays the game board of 3 columns and 3 rows.
        Dimensions declared in a variable
        """
        print(" ")
        for row in range(0, BOARD_HEIGHT):
            print(Col.BLUE + '|', end="")
            for col in range(0, BOARD_WIDTH):
                print(f"    {self.board[row][col]}" + Col.BLUE + "  |", end="")
            print("\n")
        
        print(Col.BLUE + " -"*12)

        #Displays number of columns
        for row in range(BOARD_WIDTH):
            print(Col.BLUE + f"     {row+1}   ", end="")
        print("\n")
    
    def whos_move(self) -> str:
        """
        Alternate between player's 1 and 2
        """
        pieces = ['X', 'O']
        return pieces[self.moves % 2]
    
    def winning_move(self) -> bool:
        """
        Checking if any of the rows have the same
        value BUT not the initial dash placeholder.
        If the condition is met then it ends the
        game.
        """
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_move = self.board[last_row][last_col] # X or O

        def row_win() -> bool:
            for row in range(0, BOARD_HEIGHT):
                for col in range(0, (BOARD_WIDTH)):
                    if (last_move == self.board[row][col] and
                        last_move == self.board[row][col+2]):
                        return True
            return False

        def column_win() -> bool:
            for row in range(0, (BOARD_HEIGHT)):
                for col in range(0, BOARD_WIDTH):
                    if (last_move == self.board[row][col] and
                        last_move == self.board[row+2][col]):
                        return True
            return False

        def diagonal_win() -> bool:
            for row in range(3, BOARD_HEIGHT):
                for col in range(0, (BOARD_WIDTH)):
                    if (last_move == self.board[row][col] and
                        last_move == self.board[row-1][col+1]):
                        return True
            
            for row in range(0, BOARD_HEIGHT):
                for col in range(0, (BOARD_WIDTH)):
                    if (last_move == self.board[row][col] and
                        last_move == self.board[row+1][col+1]):
                        return True

            return False

        
        if row_win() or column_win() or diagonal_win():
            cls()
            self.display_board()
            if last_move == Col.RED + 'X':
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
    A function to start the game once both players have
    signed up, and validated everything
    """
    game = Board()

    game_won = False

    while not game_won:
        cls()
        game.display_board()

        is_move_valid = False

        while not is_move_valid:
            if game.whos_move() == "X":
                print(f"{val.player1name}'s move. " +
                       "You play with " +  Col.RED + "X")
                player_move = input(f"Choose a free space between 1 - 9:\n")
            
            else:
                print(f"{val.player2name}'s move." +
                        "You play with " + Col.BLUE + "O")
                player_move = input(f"Choose a free space between 1 and 9:\n")
            
            try:
                if(int(player_move) > 0):
                    is_move_valid = game.move(int(player_move)-1)
                else:
                    print(Col.RED + "Incorrect input, please try again\n")
            except:
                print(Col.RED + f"Please choose a free space between 1 and 9.\n")
        
        game_won = game.winning_move()

        if game.moves == BOARD_HEIGHT * BOARD_WIDTH:
            cls()
            game.display_board()
            print(Col.BLUE + "\n----> The game is over - it's a tie! <----\n")

            time.sleep(2)
            separate_line()
            play_again()

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