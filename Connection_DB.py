import mysql.connector
mydb = mysql.connector.connect(host='192.168.30.10',
                              port='3306',
                              user='EGE_DEV',
                              password='EGE@P4$$wd',
                              database='',
                              auth_plugin='mysql_native_password')

db_info = mydb.get_server_info()
cursor = mydb.cursor()
cursor.execute('SELECT DATABASE();')
db = cursor.fetchall()

if mydb.is_connected():
    print('SUCCESS - Connected to database: {}, version: {}'.format(db, db_info))

else:
    print('ERROR - Unable to connect to database')
