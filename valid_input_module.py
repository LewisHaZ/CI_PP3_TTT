from email_validator import validate_email, EmailNotValidError


def input_name():
    return validation_input("Please enter your name", isValidName)


def input_email():
    return validation_input("Please enter your email", isValidEmail)


def input_number():
    return int(validation_input("Please enter a number", isValidNumber))


def validation_input(prompt, validation):
    while True:
        input_val = input(prompt)
        error_msg = validation(input_val)
        if error_msg is None:
            return input_val


def isValidName(name):
    """
    A function to validate the username against a criteria of
    2 - 12 characters and only using letters.
    @param player_name(string): Player name inputted
    """
    try:
        if len(name) < 2 or len(name) > 12:
            return "User name must be between 2 - 12 chars"
        if not name.isalpha():
            return "Player name must only contain letters"
        return None
    except TypeError:
        return "Another error occurred"


def isValidEmail(email):
    """
    A function to validate the user's email address
    against the database and the correct name convention.
    eg. Player1@example.com
    @param email(string): Player's email address.
    """
    try:
        validate_email(email)
        return None
    except EmailNotValidError as e: 
        return f'{str(e)}\nPlease type a correct email address.'


def isValidNumber(number):
    if number.isDigit():
        return None
    return ""
