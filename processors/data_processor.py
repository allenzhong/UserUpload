import csv
import MySQLdb
from MySQLdb import MySQLError, OperationalError, ProgrammingError
from user import User, EmailInvalidError

class CSVFormatInvalidError(Exception):
  def __init__(self, message):
    self.message = message

  def __str__(self):
      return self.message

class DatabaseError(Exception):
  def __init__(self, message):
    self.message = message

  def __str__(self):
    return self.message

class DataProcessor:
  def __init__(self, csv_file_name=""):
    self.csv_file_name = csv_file_name

  def fetch_data(self):
    reader = open(self.csv_file_name, 'r')
    index = 0
    users = []
    try:
      for line in csv.reader(reader):
        if index == 0:
          pass
        else:
          # should check exception that length of line less than 3
          name = line[0].strip()
          surname = line[1].strip()
          email = line[2].strip()
          user = User(name, surname, email)
          users.append(User(name, surname, email))

        index = index + 1
    except EmailInvalidError as emailErr:
      raise CSVFormatInvalidError("The format of CSV file is invalid. Check row {3}: \nName: {0} Surname: {1} Email: {2}".format(name, surname, email, index+1))
    except Exception as err:
      raise CSVFormatInvalidError("The format of CSV file is invalid.")
    return users

  def create_table(self, table_name, host, username, password, database):
    create_table_sql = ("CREATE TABLE IF NOT EXISTS `users` ("
      "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
      "  `name` varchar(50) NOT NULL,"
      "  `surname` varchar(50) NOT NULL,"
      "  `email` varchar(50) NOT NULL,"
      "  KEY `email` (`email`)"
      ") ENGINE=InnoDB")
    dbcon = MySQLdb.connect(host, username, password, database)
    cursor = dbcon.cursor()
    cursor.execute(create_table_sql) 
    cursor.close()
    dbcon.close()
 
  def insert_data(self, users, table_name, host, username, password, database, dry_run=False):
    insert_user_sql =("INSERT INTO {0} (name, surname, email) VALUES (\"{1}\", \"{2}\", \"{3}\");")
    try:
      dbcon = MySQLdb.connect(host, username, password, database)
      cursor = dbcon.cursor()
      try:
        for user in users:
          cursor.execute(insert_user_sql.format(table_name, user.name, user.surname, user.email)) 
        if dry_run:
          dbcon.rollback()
          print('[Dry run model] has been executed successfully.')
        else:
          dbcon.commit()
          print('Data has been inserted into table users.')
      except ProgrammingError as err:
        dbcon.rollback()
        print(err.args[1])

      cursor.close()
      dbcon.close()
    except OperationalError as oerr:
      print(oerr.args[1])
