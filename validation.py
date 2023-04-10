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