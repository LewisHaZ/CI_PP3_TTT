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
        print(Col.RED + "Please type your email again.\n")
    
