import csv
import MySQLdb
from user import User

class CSVFormatInvalidError(Exception):
  def __init__(self, message, errors):
    super(CSVFormatInvalidError, self).__init__(message)
    self.errors = errors

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
    except Exception: 
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
 
  def insert_data(self, table_name, users, host, username, password, database):
    insert_user_sql =("INSERT INTO {0} (name, surname, email) VALUES ('{1}', '{2}', '{3}');")
    dbcon = MySQLdb.connect(host, username, password, database)
    cursor = dbcon.cursor()
    try:
      for user in users:
        cursor.execute(insert_user_sql.format(table_name, user.name, user.surname, user.email)) 
      dbcon.commit()
    except MySQLError as err:
      print(err)
    cursor.close()
    dbcon.close()