# User Upload

## Environment

* System
  * Ubuntu 14.04 +
  * MacOS 
* Software
  * Python 2.7.6
  * MySQL 5.5.x
* Libraries


## Installation

##### MySQL

```bash
sudo apt-get update
sudo apt-get install mysql-server mysql-client
```

Then config MySQL account and password:

```bash
sudo mysql_secure_installation
```
##### Python Library

```bash
sudo apt-get -y install python-pip python-dev libmysqlclient-dev
sudo apt-get install python-mysqldb
```


## Use

##### Help
```bash
python user_upload.py -?
usage: user_upload.py [-?] [-f FILE] [-c] [-r] -u USERNAME -p PASSWORD -d
                      DATABASE [-h HOST]

Program for user import from CSV file to MySQL.

optional arguments:
  -?, --help            Output the above list of directives with details.
  -f FILE, --file FILE  Name of the CSV to be parsed
  -c, --create_table    this will cause the MySQL users table to be built (and
                        no further action will be taken)
  -r, --dry_run         this will be used with the --file directive in the
                        instance that we want to run the script but not insert
                        into the DB. All other functions will be executed, but
                        the database won't be altered.
  -u USERNAME, --username USERNAME
                        MySQL username
  -p PASSWORD, --password PASSWORD
                        MySQL password
  -d DATABASE, --database DATABASE
                        MySQL Database that will create table and insert data
  -h HOST, --host HOST  MySQL host
```

###### Example

If you have an MySQL user `test` with password `testpassword` and the target database `user_load`, and want to create table in database `user_load`, you could use command as showing below

```bash
python user_upload.py --create_table -u test -p testpassword -d user_upload
```

If you have an MySQL user `test` with password `testpassword` and the target database `user_load`, you could use this tools to upload data in  `users.csv` as following command

```bash
python user_upload.py -f users.csv -u test -p testpassword -d user_upload
```

Or if you would like change target host, just add `-h` argument

```bash
python user_upload.py -f users.csv -u test -p testpassword -d user_upload -h 192.168.1.111
```

With `-r -dry-run` arguments, it verify all execution without only insert data into database.


## Run Test

To make sure running test will be successful, please change name of  `example.test.cfg` to `test.cfg` and then change configuration in this file.

Run all test
```bash
python -m unittest discover
```

Run test for `data_processor`

```bash
python -m unittest test.test_data_processor.TestDataProcessor
```

Run test for `user`

```bash
python -m unittest test.test_user.TestUser
```
