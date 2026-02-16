import json
import sys
import os
import argparse
from datetime import datetime, date

FILE_NAME = 'data.json'

# utility
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r') as f:
        try:
            expenses = json.load(f)
            return expenses
        except json.JSONDecodeError:
            return []

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as f:
        json.dump(expenses, f, indent=4)

def get_next_id(expenses):
    if not expenses:
        return 1
    next_id = max(expense['id'] for expense in expenses) + 1
    return next_id

def validate_amount(amount):
    if amount < 0:
        print('Negative amount. Try Again')
        sys.exit(1)

# core features
def add_expense(expenses, description, amount):
    validate_amount(amount)
    id = get_next_id(expenses)
    expense = {
        'id': id,
        'description': description,
        'amount': amount,
        'date': str(datetime.now().date())
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f'Expense added successfully (ID: {id})')

def update_expense(expenses, id, description, amount):
    validate_amount(amount)
    for expense in expenses:
        if expense['id'] == id:
            expense['description'] = description
            expense['amount'] = amount
            save_expenses(expenses)
            print('Expense updated successully')
            return
    print('No matching ID found')
    
def delete_expense(expenses, id):
    for expense in expenses:
        if expense['id'] == id:
            expenses.remove(expense)
            save_expenses(expenses)
            print('Expense deleted successfully')
            return
    print('No matching ID found')

def list_expenses(expenses):
    if(len(expenses) == 0):
        print('No expenses in the data yet')
    else:
        max_col = max(len('Description'), max([len(expense['description']) for expense in expenses])) + 2
        print(f"{'ID':<5} {'Description':<{max_col}} {'Amount':<7} {'Date':<10}")
        for expense in expenses:
            id, description, amount, date = expense['id'], expense['description'], expense['amount'], expense['date']
            print(f'{id:<5} {description:<{max_col}} {amount:<7} {date:<10}')

def summarize_expenses(expenses, month):
    if month is not None:
        if month < 1 or month > 12:
            print('Invalid month input')
            return
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
    sp_add.add_argument('--description', required=True)
    sp_add.add_argument('--amount', type=int, required=True)
    sp_add.set_defaults(func=handle_add)

    sp_update = subparsers.add_parser('update')
    sp_update.add_argument('--id', type=int, required=True)
    sp_update.add_argument('--description', required=True)
    sp_update.add_argument('--amount', type=int, required=True)
    sp_update.set_defaults(func=handle_update)

    sp_delete = subparsers.add_parser('delete')
    sp_delete.add_argument('--id', type=int, required=True)
    sp_delete.set_defaults(func=handle_delete)

    sp_list = subparsers.add_parser('list')
    sp_list.set_defaults(func=handle_list)

    sp_summary = subparsers.add_parser('summary')   
    sp_summary.add_argument('--month', type=int)
    sp_summary.set_defaults(func=handle_summary)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        return
    args.func(args)

if __name__ == '__main__':
    main()