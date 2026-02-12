import json
import sys
import argparse

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