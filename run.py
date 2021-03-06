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
# calls service_account_file method of the imported Credentials class, passed argument of creds.json file
CREDS = Credentials.from_service_account_file('creds.json')
# uses with_scopes method of the CREDS object with an argument of the SCOPE variable. Links CREDS and SCOPE variables
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# uses gspread.authorize method of the gspread library. Passes argument of SCOPED_CREDS
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# uses gspread's open() method to open the love_sandwiches_spreadsheet sheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches_spreadsheet')
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
    while True:  # prevents having to restart program each time an error occurs
        print('Please enter sales data from the last market day')
        print('This data should conisist of 6 figures, each separated by commas')
        print('Example sales data: 10,20,35,29,13,19\n')

        data_string = input('Enter your data here:\n')
        #print(f'The data provided is {data_string}') # reprints user input as a check

        # grabs data_string and splits it up into a list at the commas
        sales_data = data_string.split(',')
        #print(sales_data)

        if validate_data(sales_data):  # same as saying if validate_data(sales_data) == True
            print('data is valid')
            break  # breaks out of while loop

    # returns entered and converted data to function caller - the variable called data
    return sales_data


def validate_data(values):  # values here is sales_data
    """
    Checks whether sales_data has 6 values
    Converts all of the string values of the sales_data list into integers
    Raises an error if there are not 6 values
    """
    try:
        # tries to convert entered sales data from strings into integers
        [int(value) for value in values]
        if len(values) != 6:  # checks if the sales_data variable has exactly 6 values, triggers if not 6 values
            # this is inserted as the value of e, below
            raise ValueError(
                f'6 values are required. You entered {len(values)}')

    except ValueError as e:
        # inserts the ValueError f-string from the try statement
        print(f'Invalid data: {e}. Please try again')
        return False  # returns False to the get_sales_data function

    return True  # returns true to the if statement in the get_sales_data function
    #print(sales_data)


#def update_sales_worksheet(data): # takes in the variable called data, which is the same as sales_data, the list created below this function
 #   """
  #  Update sales worksheet in love_sandwiches_spreadsheet. add new row with the list data provided
   # """
    #print('Updating sales worksheet...\n')

    #sales_worksheet = SHEET.worksheet('sales') # uses SHEET variable defined above and the gspread worksheet() method to access the sales worksheet

    #sales_worksheet.append_row(data)

    #print('sales worksheet updated \n')


#def update_surplus_worksheet(data): # data here is the same as new_surplus_data
 #   """
 #   Update surplus worksheet in love_sandwiches_spreadsheet - add new row with the data provided
 #   """
 #   print('Updating surplus worksheet...\n')

#    surplus_worksheet = SHEET.worksheet('surplus')

 #   surplus_worksheet.append_row(data)

  #  print('Surplus worksheet updated \n')


# worksheet here refers to any of the three worksheets in the love_sandwiches_spreadsheet
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Updates relevant worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully\n')


# sales_row argument is the same as sales_data
def calculate_surplus_data(sales_row):
    """
    Compare sales data with stock data and calculate the surplus of each sandwich type
    The surplus is the stock number minus the sales number
    Postive surplus numbers indicate when supply has been greater than demand, and sandwiches are thrown away
    Negative surplus numbers indicate when demand has outstripped demand, and sandwiches have been made fresh to meet that demand
    """

    print('Calculating surplus data...\n')

    # generates a list of lists - each row of the spreadsheet is a list, and these are contained as list items in another list
    stock = SHEET.worksheet('stock').get_all_values()

    # pprint(stock) # uses pprint method of external pprint library
    # slices the last value, -1 being the index of the last list in the stock list, which is a list of lists
    stock_row = stock[-1]
    # the .row_values(row-number) method is also a viable, provided that you have only a single row of data to access, or you want to access a particular row

    # print(f'stock_row: {stock_row}')
    # print(f'sales_row: {sales_row}')

    surplus_data = []  # empty list to hold surplus data
    # converts the stock_row list from a list of strings into a list of integers
    stock_row = [int(stock) for stock in stock_row]
    for stock, sales in zip(stock_row, sales_row):
        surplus = stock - sales  # instead of using the converter on line 106, we could instead wrap the singular variable called stock in the int() method, which would convert the variable when it is accessed
        surplus_data.append(surplus)
        # this is very clever - the zip method is used here to iterate through two lists at the same time
        # each item in the sales list is subtracted from the corresponding item in the stock list, with the result held in the surplus variable
        # the value of the surplus variable is then appended to the empty surplus_data variable, which is an empty list

    # returns surplus_data to the new_surplus_data variable in the main() function
    return surplus_data


def get_last_five_sales_entries():
    """
    Retrieves columns of data from sales worksheet, collecting the last 5 entries for each sandwich type
    Returns this data as a list of lists
    """
    sales = SHEET.worksheet('sales')

    columns = []  # declares empty list
    # sets up a loop that loops 6 times between 1 inclusive and 7 non-inclusive
    for index in range(1, 7):
        # retrieves the values stored in columns 1 to 6 of the sales worksheet and stores each column's values in the column variable
        column = sales.col_values(index)
        # reassigns the column variable to slice off the last 5 values using slice notation and designating the start position of the slice
        column = column[-5:]
        # appends the column variable to the columns variable
        columns.append(column)

    return columns


# data here is the sliced columns returned from the get_last_five_sales_entries
def calculate_stock_data(data):
    """
    Calculate the average sales over the last 5 days 
    """
    print('Calculating stock data...\n')

    new_stock_data = []

    for column in data:  # data is a list of lists, so column is a list that corresponds to each column retrieved from the worksheet
        # converts string values in each column to integers
        int_column = [int(num) for num in column]
        # sum adds the values of the list together to give a total, len gets the number of items in the list
        average = sum(int_column) / len(int_column)
        # since each column can only consist of 5 values, sum(int_column) / 5 would also work, but using the len() method allows for
        # flexibility is a different average needs to be calculated, such as the average over the last 7 days, for example
        stock_num = average * 1.1
        stock_num = round(stock_num)
        new_stock_data.append(stock_num)

    return new_stock_data


def get_stock_values(data):
    """
    Creates a dictionary of each sandwiches with the recommended stock of each sandwich
    """
    headings = SHEET.worksheet('stock').row_values(1) # creates list of column headings
    #dictionary = dict.fromkeys(headings, data)
    #dictionary = {}  # creates empty dictionary for later filling
    #for heading in headings: # nested loop
     #   for value in data:
      #      dictionary[heading] = value # creates key:value pair
       #     data.remove(value) # removes each value of the data list as that value is added to the dictionary
        #    break
    dictionary = {headings[i]: data[i] for i in range(len(headings))}  # Building dictionary from headings variable and data variable using dictionary comprehension

    return dictionary



def main():
    """
    Contains all main program functions
    """
    data = get_sales_data()  # calls get_sales_data function
    # does the same thing as on line 60, but actually converts into a list this time
    sales_data = [int(number) for number in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)
    update_worksheet(new_surplus_data, 'surplus')
    sales_columns = get_last_five_sales_entries()
    recommended_stock = calculate_stock_data(sales_columns)
    update_worksheet(recommended_stock, 'stock')
    stock_values = get_stock_values(recommended_stock)

    print(stock_values)


print('Welcome to Love Sandwiches Data Automation')
main()  # the function caller for main must be below where the function is defined, or the Python interpreter won't be able to execute

