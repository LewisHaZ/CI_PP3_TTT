import time
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from colors import Color as Col
from run import start_game, cls, separate_line

# Scope and constant vars defined as in love_sandwiches walk-through project
# by Code Institute
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Values for my Google sheets database
SHEET = GSPREAD_CLIENT.open('ttt_database')
WORKSHEET = SHEET.worksheet("Players")

player = ["Player1", "Player2"]

def existing_acc(players):
    """
    This function takes the existing email addresses from the spreadsheet
    and welcomes them back, other content stored in the spreadsheet is the
    score achieved and name of the user.
    """
    print(Col.BLUE + "Greetings user. " + 
        "Please enter your login details.")

        global player1name
        global player2name
        global player1score
        global player2score
        global player1email_row
        global player2email_row

        try:
            for i, player in enumrate(players):
                email = user_input_email(player)
                existing_player = is_player_registered(email)

                if existing_player:
                    if i == 0:
                        player1email_row = WORKSHEET.find(email).row
                        player1name = \
                            WORKSHEET.row_values(player1email_row)[0]
                        player1score = \
                            int(WORKSHEET.row_values(player1email_row)[2])
                        
                        print(Col.RED + f"\nHello {player1name}!\n")
                    elif i == 1:
                        player2email_row = WORKSHEET.find(email).row
                        player2name = \
                            WORKSHEET.row_values(player2email_row)[0]
                        player2score = \
                            int(WORKSHEET.row_values(player2email_row)[2])
                        print(Col.YELLOW + f"\nHello {player2name}!\n")
                    break

                else:
                    input_correct_email(player)
                
            time.sleep(2)
            start_game_message(player1name, player2name)

        except TypeError:
            return None


def user_input_email(playername: str) -> str:
    """
    A function that asks for user to input their email
    @param playername(string): Player's number
    """
    while True:
        email input(f"{playername} - What is your email address?\n").strip()

        if validate_user_input(email):
            break

    return email


def validate_user_input(email: str):
    """
    A function to validate the user's email address
    against the database and the correct name convention.
    eg. Player1@example.com
    @param email(string): Player's email address.
    """
    try:
        validate_email(email)
        return True
    
    except EmailNotValidError as e:
        print(Col.RED + "\n" + str(e))
        print(Col.RED + "Please type a correct email address.\n")
    

def is_player_registered(email: str) -> bool:
    """
    A function to verify if the player is registered
    yet. This checks against the database
    @param email(string): Player's email address.
    """
    email_column = WORKSHEET.col_values(2)

    if email in email_column
        return True
    else:
        return False


def input_correct_email(player: str):
    """
    A function to notify the player they have not 
    typed a valid registered email address and 
    nothing was found in the database.
    @param player(sting): number of current player
    """
    print(Col.RED + "\nSorry, this email isn't registered with us.\n")
    selected_option = email_not_registered()

    if selected_option == "1":
        print("Please type the email address again:")
    
    elif selected_option == "2":
        register_account(player)


def email_not_registered() -> str:
    """
    A function to give the option to enter another email or
    to create a new email and user.
    """
    time.sleep(1)
    print(Col.BLUE + "Do you want to:")
    options = "1. Try another email\n2. Create a new user\n"
    selected_option = input(options)
    separate_line()

    while selected_option not in ("1", "2"):
        print("Please choose from 1 or 2")
        selected_option = input(options)

        separate_line()
    
    return selected_option


def register_single_player(player_number: str):
    """
    A function to register one player.
    @param player_number(string): number of player
    """

    time.sleep(1)
    print(Col.YELLOW + "Creating a new account for you...")
    print(" ")
    print(" ")
    new_player = player_number
    player_info = create_new_players(new_player)
    update_players_worksheet(player_info)

def register_new_players(players):
    """
    A function to register a new player, asks for 
    an input in terms of name. Saved to a variable,
    it will be displayed in game to indicate the 
    players' turn.
    """

    global player1name
    global player2name
    global player1score
    global player2score
    global player1email_row
    global player2email_row

    time.sleep(1)
    print(Col.YELLOW + "Beginning registration process...")
    print(" ")

    try:
        while True:
            for i, player in enumerate(players):
                if i == 0:
                    player_1_info = create_new_players(player)
                    update_players_worksheet(player_1_info)
                    player1name = player_1_info[0]
                    player1score = player_1_info[2]
                    player1email_row = WORKSHEET.find(player_1_info[1]).row
                
                elif i == 1
                    player_2_info = create_new_players(player)
                    update_players_worksheet(player_2_info)
                    player2name = player_2_info[0]
                    player2score = player_2_info[2]
                    player2email_row = WORKSHEET.find(player_2_info[1]).row
                break

            separate_line()
            print(f"Thank you {player1name} & {player2name}, " +
                    "your details have been added and registered.\n")
            
            time.sleep(2)
            start_game_message(player1name, player2name)
            separate_line()
        
        except TypeError:
            return None


def create_new_players(player_number: str) -> list:
    """
    A function to create a new player, this gets
    the player's inputted name and email and checks 
    if it is already in the database.
    @param player_number(string): number of the player
    """

    email_column = WORKSHEET.col_values(2)

    while True:
        player = input(f"{player_number} - what would you like to be called?\n")
        print(" ")

        if validate_username(player):
            break
    
    while True:
        player_email = user_input_email(player)
    
        if player_email not in email_column:
            print(Col.YELLOW + "\nThank you.\n")
            break

        else:
            print(Col.RED + f"\nSorry {player} , this email is already in use.")
            print(Col.RED + "Please try again.\n")
    
    return [player, player_email, 0]


def validate_username(player_name: str) -> bool:
    """
    A function to validate the username against a criteria of
    2 - 12 characters and only using letters.
    @param player_name(string): Player name inputted
    """
    try:
        if len(player_name) < 2 or len(player_name) > 12:
            print(Col.RED + "User name must be" + 
            "2 - 12 letters long.")
            print(Col.RED + "Please enter another name.\n")
        
        elif not player_name.isalpha():
            print(Col.RED + "Player name must only contain letters." +
                "Please enter another name.\n")

        else:
            return True

        except TypeError:
            return False
            