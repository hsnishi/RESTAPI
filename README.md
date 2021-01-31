# REST API
This project contains the source code of a REST JSON API
which implements the methods GET, POST, PUT and DELETE
to operate on a database.
This database contains the information about developers
with the structure bellow.

id - integer
name - string
gender - string
age - integer
hobby - string
date of birth - string

## Create and config the virtual environment
To create a new virtual enviroment
python -m venv <path + name of virtual environment>

To activate the virtual environment execute the command bellow.
Windows - <path + name of virtual environment>\Script\activate
Ubuntu - source <path + name of virtual environment>\bin\activate

Install the dependencies of the project.
pip install -r requirements.txt

## Populate the database
There are some examples of developers in the file developers.csv.
So in order to populate the database you just need to run the python
script populate.py. This file will read the csv file and send the
request command to the Flask server which will use the SQLAchemy to
populate the database used in this project.

Steps:
1 -  Open a terminal and navigates to the folder app
2 - Execute the Flask server - "python app.py"
3 - Open another terminal to execute the unit test
4 - Navigate to the root project folder
5 - Execute the command - "python populate.py"

After execute the steps above, the file developers.db will be created with 
the examples from csv file.

## Execute the main application
WIP

## Unit Test
In order to execute the Unit test, please follow the steps below.
1 - Delete the existing database - "developers.db"
2 - Open a terminal and navigates to the folder app
3 - Execute the Flask server - "python app.py"
4 - Open another terminal to execute the unit test
5 - Navigate to the test folder
6 - Execute the command - "python test_app.py" 