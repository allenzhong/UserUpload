import unittest
import ConfigParser
import io
import MySQLdb
from processors.data_processor import DataProcessor

TESTING_CONFIG = 'test/test.cfg'
TESTING_CSV = 'test/example.csv'
NUMBER_OF_ROW_IN_CSV = 5
DATABASE_NAME = 'test_user_upload'
TABLE_NAME = 'user'

class TestDataProcessor(unittest.TestCase):
  def setUp(self):
    self.config = ConfigParser.ConfigParser()
    self.config.readfp(open(TESTING_CONFIG))
    self.username = self.config.get('mysqld', 'username')
    self.password = self.config.get('mysqld', 'password')
    self.host = self.config.get('mysqld', 'host')

    self.dbcon = MySQLdb.connect(self.host, self.username, self.password)
    self.cursor = self.dbcon.cursor()
    create_db_sql = 'CREATE DATABASE_NAME IF NOT EXISTS ' + DATABASE_NAME
    self.cursor.execute(create_db_sql)
    self.dbcon.commit()
    self.cursor.close()
    self.dbcon.close()
    raw_csv = """name,surname,email  
John,smith,jsmith@gmail.com
HaMish,JONES,ham@seek.com
Phil ,CARRY   ,phil@open.edu.au  
Johnny,O'Hare,john@yahoo.com.au"""
    csv_file = open(TESTING_CSV, 'w')
    csv_file.write(raw_csv)
    csv_file.close()

  def tearDown(self):
    try:
      os.remove(TESTING_CSV)
    except OSError:
      pass

  def test_read_data_from_csv_file_with_filename(self):
    processor = DataProcessor(TESTING_CSV)
    users = processor.fetch_data()
    self.assertEqual(users.count, NUMBER_OF_ROW_IN_CSV)

  def test_create_table_in_specified_db_with_user_and_pwd(self):
    processor = DataProcessor(TESTING_CSV)
    processor.create_table(TABLE_NAME, self.username, self.password)
    #fetch database shoudl find user table

    self.cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(TABLE_NAME.replace('\'', '\'\'')))

    self.assertEqual(self.cursor.fetchone()[0], 1)


  def test_insert_data_into_table_existing(self):
    #create table with mysql connector
    dbcon = MySQLdb.connect(self.host, self.username, self.password, DATABASE_NAME)
    cursor = dbcon.cursor()
    create_table_sql = 'CREATE DATABASE_NAME IF NOT EXISTS ' + DATABASE_NAME
    cursor.execute(create_db_sql)

    dbcon.commit()

    #check inserted data available
    user = User('Allen', 'Allen', 'allen@email.com')
    processor = DataProcessor()
    processor.insert_data([user])

    query_data_sql = 'SELECT count(*) FROM ' + DATABASE_NAME
    cursor.execute(query_data_sql)
    results = cursor.fetchall()
    self.assertGreater(results.count, 0)
    cursor.close()
    dbcon.close()

