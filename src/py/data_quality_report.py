'''
    Author: Cloyd Van S. Secuya
    Filename: data_quality_report.py
    Date of Creation: July 14, 2022
    Description:
        Just like data_quality_check this also generates test cases to find anomalies in the database.
        This produces an output file to the test DIR, named testcase_results.csv
'''

from lib2to3.pgen2.token import NEWLINE
import os
import pandas as pd
import csv
from tabulate import tabulate
import mysql.connector
from mysql.connector import Error

import testcases
from data_migration_checks import check_for_nulls
from data_migration_checks import check_for_min_max
from data_migration_checks import check_for_valid_values
from data_migration_checks import check_for_duplicates
from data_migration_checks import run_data_quality_check

# Output direction
file_name_path = 'test/testcase_results.csv'

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
print(results)                  # Print the results to console

df=pd.DataFrame(results)        # Place it in a dataframe
df.index+=1                     # Set index to 1 to move past headers
df.columns = ['Test Name', 'Table','Column','Test Passed']
# Begin save test out file in .csv
saveToFile = open(f'{file_name_path}', 'w', newline='')     # Create a new file
header = ['Test Name', 'Table','Column','Test Passed']
writer = csv.writer(saveToFile)
writer.writerow(header)         # header column, index=0
writer.writerows(results)       # rows, index=1
save_table = tabulate(df,headers='keys',tablefmt='mysql')

print(save_table)
# End of data quality checks

# End connection to database
connection.close()
print("\n\nExit connection at Jester_DB")
print(f'Saved to {file_name_path}')