import json
import sys
import argparse
from datetime import datetime

FILE_NAME = 'data.json'

# utility
def load_expenses():
    with open('r', FILE_NAME) as f:
        expenses = json.load(f)
        return expenses

def save_expenses(expenses):
    with open('w', FILE_NAME) as f:
        json.dump(expenses, f, indent=4)

def get_next_id(expenses):
    next_id = max(expense['id'] for expense in expenses) + 1
    return next_id

# core features

def add_expense(expenses, description, amount):
    expense = {
        'id': get_next_id(expenses),
        'description': description,
        'amount': amount,
        'timestamp': datetime.date()
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
            expenses = expenses.remove(expense)
            save_expenses(expenses)
            break


def main():
    expenses = load_expenses(FILE_NAME)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    sp_add = subparsers.add_parser('add')
    sp_add.add_argument('--description')
    sp_add.add_argument('--amount', type=int)

    sp_update = subparsers.add_parser('update')
    sp_update.add_argument('--id', type=int)

    sp_delete = subparsers.add_parser('delete')
    sp_delete.add_argument('--id', type=int)

    sp_list = subparsers.add_parser('list')

    sp_summary = subparsers.add_parser('summary')   
    sp_summary.add_argument('--month', type=int)

    args = parser.parse_args()

    print(args.description, args.amount)

    #json 

    file = json.load('data.json')
    

if __name__ == '__main__':
    main()