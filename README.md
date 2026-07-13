# Python Contact Manager

A beginner-friendly command-line contact management application built with Python.

This project allows users to add, display, search and delete contacts. Contact information is stored locally in a text file so that it remains available after the program is closed.

## Project Objective

The objective of this project was to practise the fundamental concepts of Python by building a simple but functional application.

Through this project, I worked with:

* Variables and data types
* User input and output
* Conditional statements
* Loops
* Functions
* Lists and dictionaries
* Python modules
* File reading and writing
* Exception handling

## Features

The application currently allows users to:

* Add a new contact
* Display all saved contacts
* Search for a contact by name
* Delete a contact
* Save contacts locally in a text file
* Handle the absence of a contact file

Each contact contains:

* Name
* Telephone number
* Email address

## Project Structure

```text
gestionnaire_de_contacts/
├── index.py
├── ajout_contact.py
├── afficher_contacts.py
├── rechercher_contact.py
├── supprimer_contact.py
├── contacts.example.txt
├── .gitignore
└── README.md
```

### File descriptions

* `index.py`: displays the main menu and controls the application.
* `ajout_contact.py`: adds and saves a new contact.
* `afficher_contacts.py`: displays all saved contacts.
* `rechercher_contact.py`: searches for a contact by name.
* `supprimer_contact.py`: deletes a contact from the contact file.
* `contacts.example.txt`: provides an example of the expected contact format.

## Requirements

* Python 3
* No third-party packages are required

## Installation

Clone the repository:

```bash
git clone https://github.com/yacintheb/gestionnaire_de_contacts.git
```

Open the project folder:

```bash
cd gestionnaire_de_contacts
```

## Running the Application

Run the main Python file:

```bash
python index.py
```

On some Windows installations, use:

```bash
py index.py
```

The following menu will be displayed:

```text
======== CONTACT MANAGER ========

1. Display contacts
2. Add a contact
3. Delete a contact
4. Search for a contact
5. Exit
```

Enter the number corresponding to the action you want to perform.

## Data Storage

Contacts are stored locally in a file named `contacts.txt`.

This file is excluded from GitHub through `.gitignore` because it may contain personal information. A `contacts.example.txt` file is provided to demonstrate the expected data format.

## Current Limitations

This is a beginner learning project. The current version:

* Uses a command-line interface
* Stores data in a text file rather than a database
* Searches contacts by name
* Does not yet allow contacts to be edited
* Does not include automated tests

## Planned Improvements

Future improvements may include:

* Editing an existing contact
* Validating telephone numbers and email addresses
* Preventing duplicate contacts
* Making searches case-insensitive
* Storing contacts in CSV or JSON format
* Adding automated tests
* Improving the command-line interface
* Creating a graphical or web interface

## Author

**Yacinthe Bitchoka**

GitHub: `@yacintheb`

## Project Status

This project is part of my progressive learning journey in Python and software development.
