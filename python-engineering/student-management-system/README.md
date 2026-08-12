# Tiny Student Management System

A beginner Python project built to practice file handling, JSON, `pathlib`, functions, lists, and dictionaries.

## Features

* Add a student
* View saved students
* Store student data persistently in a JSON file

## Concepts Practiced

* Python functions
* Lists and dictionaries
* `pathlib`
* Reading and writing files
* JSON serialization and deserialization
* Persistent data storage

## How It Works

Student data is stored in `students.json`.

When the program starts, it loads the existing student data from the JSON file.

When a new student is added, the updated Python list is converted to JSON and written back to the file.

```text
students.json
      ↓
read_text()
      ↓
json.loads()
      ↓
Python list
      ↓
add/update data
      ↓
json.dumps()
      ↓
write_text()
      ↓
students.json
```

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Follow the menu:

```text
1. Add student
2. View students
3. Exit
```

## Technologies

* Python
* JSON
* pathlib
* File I/O
