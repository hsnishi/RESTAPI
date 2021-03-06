# REST API
This project contains the source code of a REST JSON API
which implements the methods GET, POST, PUT and DELETE
to operate on a database.
This database contains the information about developers
with the structure bellow.<br />

id - integer<br />
name - string<br />
gender - string<br />
age - integer<br />
hobby - string<br />
date of birth - string<br />

## Create and config the virtual environment
To create a new virtual enviroment
python -m venv <path + name of virtual environment>

To activate the virtual environment execute the command bellow.
Windows - <path + name of virtual environment>\Script\activate
Ubuntu - source <path + name of virtual environment>\bin\activate

Install the dependencies of the project.
pip install -r requirements.txt

You need to activate the virtual environment every time that you open a
new terminal.

## Populate the database
There are some examples of developers in the file developers.csv.
So in order to populate the database you just need to run the python
script populate.py. This file will read the csv file and send the
request command to the Flask server which will use the SQLAchemy to
populate the database used in this project.<br />

Steps:<br />
1 -  Open a terminal and navigates to the folder app<br />
2 - Execute the Flask server - "python app.py"<br />
3 - Open another terminal to execute the unit test<br />
4 - Navigate to the root project folder<br />
5 - Execute the command - "python populate.py"<br />

After execute the steps above, the file developers.db will be created with 
the examples from csv file.

## Execute the main application
To run the main application follow the steps bellow<br />
1 - Open a terminal and navigates to the folder app<br />
2 - Execute the Flask server - python app.py<br />
3 - Open another terminal and navigate to the project root folder<br />
4 - Populate the database executing the command - python populate.py<br />
5 - Execute the main application the request_application.py<br />

You do not need to write the URL, you just need to use the menu and write the right 
information to do the actions. The application will do the request to the server and it
will return the result.

## Unit Test
In order to execute the Unit test, please follow the steps below.<br />
1 - Delete the existing database - "developers.db"<br />
2 - Open a terminal and navigates to the folder app<br />
3 - Execute the Flask server - "python app.py"<br />
4 - Open another terminal to execute the unit test<br />
5 - Navigate to the test folder<br />
6 - Execute the command - "python test_app.py" <br />
