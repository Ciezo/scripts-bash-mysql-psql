'''
    Author: Cloyd Van S. Secuya
    Filename: data_migration_checks.py
    Date of Creation: July 14, 2022
    Description:
         Functions for invoking in the testcases for both data quality check and reporting.
         Perform data migration check here to make sure that jester_db is filled in during self_init!
'''

# Start measuring CPU time
from time import time,ctime


# Define attribute for Connection
connection = None

# Begin running all the test cases
def run_data_quality_check(**options):
    # Horizontal rule
    print("=" * 150)

    # Print current CPU time
    print(ctime(time()))
    # Start clock monitoring
    start_time = time()
    
    # Get the pointed reference of testname define in testcases.py
    testname = options.pop("testname")
    # Invoke the type of test define from here.
    test = options.pop("test")
    
    # Measures of status and time
    print(f"Starting current automated job ---> UNIT TEST: {testname}")
    status = test(**options)
    print(f"Job Finished, Executed in: {ctime(time())} ---> UNIT TEST: {testname}")
    print(f"Test Passed {status}")
    # Capture the current time as end
    end_time = time()
    
    # Get the connection pointed as reference from the other scripts of data_quality_check and data_quality_report
    options.pop("conn")
    # Print the return parameters
    print("Test Parameters")
    for key,value in options.items():
        print(f"{key} = {value}")

    # Measure the duration of the test case execution
    print()
    print("Duration : ", str(end_time - start_time))
    # Print CPU time
    print(ctime(time()))
    # Horizontal rule
    print("=" * 150)
    # Return the testname, tablename from DB, and column from, db
    return testname,options.get('table'),options.get('column'),status




# Check all rows if there is null record based on PK of that table
def check_all_rows(table, column, conn=connection):
    SQL=f'SELECT * FROM {table} where {column} is null'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    for db in cursor:
        print(db)
    cursor.close()
    return bool(row_count)




# Check for distinct values of null in any field and row
def check_for_nulls(column,table,conn=connection):
    SQL=f'SELECT count(*) FROM {table} where {column} is null'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)




# Check of minimum and maximum assigned values of PK for each table
def check_for_min_max(column,table,minimum,maximum,conn=connection):
    SQL=f'SELECT count(*) FROM {table} where  {column} < {minimum} or {column} > {maximum}'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)




# Check if there are indeed entries in the Jester_DB where there should be
# valid values of user records and music_dir records
def check_for_valid_values(column, table, valid_values=None,conn=connection):
    SQL=f'SELECT distinct({column}) FROM {table}'
    cursor = conn.cursor()
    cursor.execute(SQL)
    result = cursor.fetchall()
    print(result)
    actual_values = {x[0] for x in result}
    print(actual_values)
    status = [value in valid_values for value in actual_values]
    print(status)
    cursor.close()
    return all(status)




# Find if there are any duplicated records in our rows. 
def check_for_duplicates(column,table,conn=connection):
    SQL=f'SELECT count({column}) FROM {table} group by {column} having count({column}) > 1'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    print(row_count)
    cursor.close()
    return not bool(row_count)