# Book Library Management System

A simple **Book Library Management System** built with Python. The project uses **JSON** to store book data and provides a command-line menu for managing books.

## Features

* Add a new book
* View all books
* Search for a book by title
* Remove a book using its ID
* Store book data in `books.json`
* Handle missing or invalid JSON files using exception handling

## Technologies Used

* Python
* JSON

## Project Structure

```text
Library/
├── lib.py
├── books.json
└── README.md
```

## How to Run

Make sure Python is installed, then run:

```bash
python lib.py
```

The program will display a menu:

```text
===== Book Library =====

1. Add Book
2. View Books
3. Search Book
4. Remove Book
5. Exit
```

Enter the corresponding number to perform an operation.

## Data Storage

Book information is stored in `books.json`.

Each book contains:

* Book ID
* Title
* Author
* Publication year

Example:

```json
{
    "101": {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988
    }
}
```

## What I Practiced

This project helped me practice:

* Functions
* Dictionaries
* Loops and conditionals
* File handling
* JSON serialization and deserialization
* Exception handling
* Basic CRUD operations

## Author

**Shriyans**
