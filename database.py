from user_module import User
import gspread
from google.oauth2.service_account import Credentials


class Database():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    def __init__(self):
        # Scope and constant vars defined in love_sandwiches project
        # by Code Institute

        creds = Credentials.from_service_account_file('creds.json')
        scoped_creds = creds.with_scopes(self.scope)
        gspread_client = gspread.authorize(scoped_creds)

        # Values for my Google sheets database
        sheet = gspread_client.open('ttt_database')
        self.worksheet = sheet.worksheet("Players")
    
    def does_user_exist(self, email):
        return email in self.worksheet.col_values(2)
    
    def get_user(self, email):
        row = self.worksheet.row_values(self.get_user_row_number(email))
        return User(row[0], row[1], row[2])
    
    def add_user(self, user):
        self.worksheet.append_row([user.name, user.email, user.score])
    
    def update_user(self, user):
        row_number = self.get_user_row_number(user.email)
        self.worksheet.update_cell(row_number, 1, user.name)
        self.worksheet.update_cell(row_number, 2, user.email)
        self.worksheet.update_cell(row_number, 3, user.score)
            
    def get_user_row_number(self, email):
        return self.worksheet.find(email, None, 2).row