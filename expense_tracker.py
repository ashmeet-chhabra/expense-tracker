import json
import sys
import argparse
from datetime import datetime, date

FILE_NAME = 'data.json'

# utility
def load_expenses():
    with open(FILE_NAME, 'r') as f:
        expenses = json.load(f)
        return expenses

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as f:
        json.dump(expenses, f, indent=4)

def get_next_id(expenses):
    if not expenses:
        return 1
    next_id = max(expense['id'] for expense in expenses) + 1
    return next_id

# core features
def add_expense(expenses, description, amount):
    expense = {
        'id': get_next_id(expenses),
        'description': description,
        'amount': amount,
        'date': str(datetime.now().date())
    }
    expenses.append(expense)
    save_expenses(expenses)

def update_expense(expenses, id, description, amount):
    for expense in expenses:
        if expense['id'] == id:
            expense['description'] = description
            expense['amount'] = amount
            save_expenses(expenses)
            break

def delete_expense(expenses, id):
    for expense in expenses:
        if expense['id'] == id:
            expenses.remove(expense)
            save_expenses(expenses)
            break

def list_expenses(expenses):
    for expense in expenses:
        id, description, amount, date = expense.values()
        print(id, description, amount, date)

def summarize_expenses(expenses, month=None):
    if month:
        filtered_total = 0
        for expense in expenses:
            if date.fromisoformat(expense['date']).month == month:
                filtered_total += expense['amount']
        print(f'Total expenses for month {month}: ${filtered_total}')
    else:
        total_expense = sum(expense['amount'] for expense in expenses)
        print(f'Total expenses: ${total_expense}')

# argparse handlers
def handle_add(args):
    expenses = load_expenses()
    add_expense(expenses, args.description, args.amount)

def handle_update(args):
    expenses = load_expenses()
    update_expense(expenses, args.id, args.description, args.amount)

def handle_delete(args):
    expenses = load_expenses()
    delete_expense(expenses, args.id)
    
def handle_list(args):
    expenses = load_expenses()
    list_expenses(expenses)

def handle_summary(args):
    expenses = load_expenses()
    summarize_expenses(expenses, args.month)

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    sp_add = subparsers.add_parser('add')
    sp_add.add_argument('--description')
    sp_add.add_argument('--amount', type=int)
    sp_add.set_defaults(func=handle_add)

    sp_update = subparsers.add_parser('update')
    sp_update.add_argument('--id', type=int)
    sp_update.set_defaults(func=handle_update)

    sp_delete = subparsers.add_parser('delete')
    sp_delete.add_argument('--id', type=int)
    sp_delete.set_defaults(func=handle_delete)

    sp_list = subparsers.add_parser('list')
    sp_list.set_defaults(func=handle_list)

    sp_summary = subparsers.add_parser('summary')   
    sp_summary.add_argument('--month', type=int)
    sp_summary.set_defaults(func=handle_summary)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()





