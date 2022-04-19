# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
# Below are Constants, which are special variables. Their CAPITAL names indicate to other developers that they are not to be tinkered with
CREDS = Credentials.from_service_account_file('creds.json') # calls service_account_file method of the imported Credentials class, passed argument of creds.json file
SCOPED_CREDS = CREDS.with_scopes(SCOPE) # uses with_scopes method of the CREDS object with an argument of the SCOPE variable. Links CREDS and SCOPE variables
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) # uses gspread.authorize method of the gspread library. Passes argument of SCOPED_CREDS
SHEET = GSPREAD_CLIENT.open('love_sandwiches_spreadsheet')   # uses gspread's open() method to open the love_sandwiches_spreadsheet sheet
# In other cases, the value passed above must match the filename of the target document exactly

# This is confusing for me at the moment - the idea behind all of these variables and method is that they are necessary to link the project to the spreadsheet, 
# and hence allow data to be pulled from the spreadsheet and posted to it
#

# the three lines below are checkers that check that the project has been set up correctly and can access the spreadsheet data:
#sales = SHEET.worksheet('sales') # uses the worksheet() method of the SHEET variable above to access the sales tab of the spreadsheet

#data = sales.get_all_values() # gets all of the data in the sales tab of the spreadsheet

#print(data) # prints the sales tab data - each row is rendered as a list in square brackets, with the values as strings

def get_sales_data():
    """
    Get Sales figures from the user
    """

    print('Please enter sales data from the last market day')
    print('This data should conisist of 6 figures, each separated by commas')
    print('Example sales data: 10,20,35,29,13,19\n')

    data_string = input('Enter your data here: ')
    print(f'The data provided is {data_string}')

get_sales_data()