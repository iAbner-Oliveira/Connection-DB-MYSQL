<h1 align="left"> PYTHON - Database Connection </h1>

Script created in python to validate connection with the database

## :snake: Functionality for Script.

- `Functionality 1`: Validate connection to MySQL database

## Setup

### Python Version

It is recommended that for full script functionality the Python version is `3.9` or higher.

### Install and add to the following Python libraries;

```MySQL Connector
pip install mysql.connector
```

### If you don't have PIP installed, run this command:

For Debian-based distributions
```
apt-get install python-pip
```
For RedHat-based distributions
```
yum install python-pip
```

<hr>



## :snake: Script

```python
import mysql.connector

# Set database connection parameters
mydb = mysql.connector.connect(host='<ip>',# Example: 187.134.10.98
                              port='<port>', # Example 3306
                              user='<user>',# Example: pyuser
                              password='<password>', # Example: pypass
                              database='<database>', # Example: pydb
                              auth_plugin='mysql_native_password')  # Plugin for active connections (Linux), if you use non-native connections, delete this line

db_info = mydb.get_server_info()
cursor = mydb.cursor()

# Command to be executed inside the database
cursor.execute('SELECT DATABASE();')
db = cursor.fetchall()

# Conditioning framework to validate database connection

if mydb.is_connected():
    print('SUCCESS - Connected to database: {}, version: {}'.format(db, db_info))

else:
    print('ERROR - Unable to connect to database')

```
