# Expense Tracker CLI

A simple command-line expense manager built with Python that allows users to add, update, delete, and summarize expenses directly from the terminal.

This project focuses on practicing file handling, JSON data storage, command-line interfaces, input validation, and structured program design.

## Project URL

https://roadmap.sh/projects/expense-tracker

---

## Features

* Add new expenses with description and amount
* Update existing expenses
* Delete expenses by ID
* List all recorded expenses
* View total expense summary
* View monthly expense summary (current year)
* Automatic date tracking for each expense
* Persistent storage using a local JSON file
* Graceful error handling and input validation

---

## Requirements

* Python 3.x
* No external libraries required

---

## Installation

Clone the repository:

```
git clone https://github.com/ashmeet-chhabra/expense-tracker
cd expense-tracker
```

(Optional) Make the script executable on macOS/Linux:

```
chmod +x expense_tracker.py
```

---

## Usage

Run the script from the terminal:

```
python expense_tracker.py <command> [arguments]
```

---

## Commands

### Add an Expense

```
python expense_tracker.py add --description "Lunch" --amount 200
```

### Update an Expense

```
python expense_tracker.py update --id 1 --description "Dinner" --amount 300
```

### Delete an Expense

```
python expense_tracker.py delete --id 1
```

### List All Expenses

```
python expense_tracker.py list
```

### View Total Summary

```
python expense_tracker.py summary
```

### View Monthly Summary

```
python expense_tracker.py summary --month 2
```

---

## Data Storage

Expenses are stored locally in a `data.json` file created automatically in the project directory.

Example structure:

```
{
    "id": 1,
    "description": "Lunch",
    "amount": 200,
    "date": "2026-02-16"
}
```

---

## License

This project is open-source and available under the MIT License.
