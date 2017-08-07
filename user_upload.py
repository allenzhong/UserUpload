import argparse
from processors.user import User
from processors.data_processor import DataProcessor, DatabaseError

def parse_arguments():
  parser = argparse.ArgumentParser(add_help=False, description='Program for user import from CSV file to MySQL.')

  parser.add_argument('-?', '--help', action='help', help='Output the above list of directives with details.',)
  parser.add_argument('-f', '--file', help='Name of the CSV to be parsed', )
  parser.add_argument('-c', '--create_table', action='store_true', help='this will cause the MySQL users table to be built (and no further action will be taken)')
  parser.add_argument('-r', '--dry_run', action='count', help='this will be used with the --file directive in the instance that we want to run the script but not insert into the DB. All other functions will be executed, but the database won\'t be altered.')
  parser.add_argument('-u', '--username', required=True, help='MySQL username')
  parser.add_argument('-p', '--password', required=True, help='MySQL password')
  parser.add_argument('-d', '--database', required=True, help='MySQL Database that will create table and insert data')
  parser.add_argument('-h', '--host', default='localhost', help='MySQL host, default is localhost')

  args = parser.parse_args()
  handle_process(args)


def create_table(args):
  try:
    processor = DataProcessor()
    processor.create_table(table_name="users", host=args.host, username=args.username, password=args.password, database=args.database)
    print('Table users has been created successfully.')
  except Exception as err:
    print(err)

def handle_process(args):
  filename = args.file
  host = args.host
  username = args.username
  password = args.password
  database = args.database
  if args.create_table:
    create_table(args)
    return
  elif filename is not None:
    processor = DataProcessor(filename)
    users = processor.fetch_data()
    processor.insert_data(users, table_name="users", host=host, username=username, password=password, database=database, dry_run=(args.dry_run > 0))

if __name__=="__main__":
  try:
    parse_arguments()
  except Exception as err:
    print(err.message)

