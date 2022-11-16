'''
    Author: Cloyd Van S. Secuya
    Filename: self_init.py
    Date of Creation: July 14, 2022
    Description:
        Self init MySQL on the localhost machine. 
        Run this script if database checks and data quality checks are needed
'''

import os
import mysql.connector
from mysql.connector import Error

connection = None

try:
    # Attempt to get password of MySQL server hosted on local machine
    # mySqlpassword = input("Enter password: ")

    mySqlpassword = os.environ.get('MYSQL_PWD')
    print("Trying to retrieve native_sql_password...PASSWD returned: ", mySqlpassword)
    connection = mysql.connector.connect(user = 'root',
                                         passwd = 'cloyd27feb2002',     # please put YOUR PASSWORD HERE
                                         auth_plugin = 'mysql_native_password',
                                         host = '127.0.0.1',
                                         port = 3306,
                                         database = 'Jester_DB')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("\nError while connecting to MySQL", e)
    print("\nTry entering YOUR PASSWORD on YOUR LOCAL MACHINE")
    print("\nCheck /scripts/self_init.py")

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")