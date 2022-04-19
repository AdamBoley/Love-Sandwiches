![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome AdamBoley,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


Index.js, package.json, Procfile, controllers folder and views folder do not need to be changed

This project uses the Google Drive API and Google Sheets API
Google Drive API:
Service account name: Love-Sandwiches
Service account ID: love-sandwiches

Creds.json is the file generated from the Google Drive API

The love_sandwiches_spreadsheet that this project accesses and updates is in my personal Google Drive
It has been shared with the Client Email value in the creds.json file

Creds.json has been added to the gitignore file, so it will never been shared to Github and thus it and its contents will remain secret

Since the creds.json file is not shared with Github, it effectively only exists in the Gitpod workspace

Hence, new workspaces will not contain the creds.json file, so it will need to be re-uploaded. This particular workspace has been pinned, so use that to access the workspace and preserve the creds.json file

This project uses two external Python libraries - google-auth and gspread

Google-auth uses the creds.json file to set up the authenication

gspread is used to access and update the information in the love_sandwiches_spreadsheet file

These libraries are installed with the terminal command `pip3 install gspread google-auth`

This project needs the entire gspread library, so `import gspread` has been added to the run.py file

It also needs the Credentials class from the service_account function, so `from google.oauth2.service_account import Credentials` has been added to the run.py file


This is a command line project, so the terminal is run using the `python3 run.py` command. This runs the code in the run.py file. 

User Stories - what should the project do?

1. Collect sales data from the user

2. Add sales data into worksheet

3. Calculate surplus numbers

4. Add surplus data to wurplus worksheet

5. Calculate the average sales for the last 5 days

6. Add calculated stock numbers into the stock worksheet

7. Print stock recommendations

8. Check that all user inputs are valid


Collecting sales data from the user

The project is set to expect sales data from the user in the csv format - comma-separated values

This allows data to be saved in a table format - useful for spreadsheets