'''
    Author: Cloyd Van S. Secuya
    Filename: data_quality_check.py
    Date of Creation: July 14, 2022
    Description:
         Script for generating data quality report and print to console. 
         All test cases function are invoked here. And this is how we can check if our newly installed records in 
         our Jester_DB do not have any anomalies
         This does not produce any output.
'''

import os
import mysql.connector
import pandas as pd
from tabulate import tabulate

import testcases
# import the data_migration_checks
from data_migration_checks import check_for_nulls
from data_migration_checks import check_for_min_max
from data_migration_checks import check_for_valid_values
from data_migration_checks import check_for_duplicates
from data_migration_checks import run_data_quality_check
from data_migration_checks import check_all_rows

# Try to retrieve any existing environment variables from localhost system 
mySqlpassword = os.environ.get('MYSQL_PWD')
# Begin connection to database
connection = mysql.connector.connect(user = 'root',
                                     passwd = 'cloyd27feb2002',     # please put YOUR PASSWORD HERE
                                     auth_plugin = 'mysql_native_password',
                                     host = '127.0.0.1',
                                     port = 3306,
                                     database = 'Jester_DB')

print("Connected to Jester_DB")

# Start of data quality checks
results = []
tests = {key:value for key,value in testcases.__dict__.items() if key.startswith('test')}
for testname,test in tests.items():
    test['conn'] = connection
    results.append(run_data_quality_check(**test))
    # check_all_rows("jester_users",connection)
print(results)

df=pd.DataFrame(results)        # Place in the dataframe
df.index+=1                     # Set index to point after header
df.columns = ['Test Name', 'Table','Column','Test Passed']
# Print to terminal direct results of test cases.
print(tabulate(df,headers='keys',tablefmt='mysql'))


#End of data quality checks
connection.close()
print("Disconnected from Jester_DB")