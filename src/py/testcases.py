'''
    Author: Cloyd Van S. Secuya
    Filename: testcases.py
    Date of Creation: July 14, 2022
    Description:
        Test cases to individually run all data quality checks.
		This script can be have newly added test cases if there are new tables.
'''

from data_migration_checks import check_for_nulls
from data_migration_checks import check_for_min_max
from data_migration_checks import check_for_valid_values
from data_migration_checks import check_for_duplicates
from data_migration_checks import check_all_rows

'''
	Unit test cases: 
		Description: This is helpful to check our MySQL database that there are no anomalies in the records
		Syntax:
			
			test={
				"testname": 	name of the test case function
				"test": 		test function
				"column":		column of the table. THIS NEEDS TO SELECT THE PK OF THE TABLE!
				"table":		table to select
			}
	@Cloyd
'''

test1={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "ID_auth",
	"table": "jester_users"
}

test2={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "music_ID",
	"table": "jester_music"
}

test3={
	"testname":"Check for all rows",
	"test":check_all_rows,
	"column": "ID_auth",
	"table": "jester_users"
}

test4={
	"testname":"Check for all rows",
	"test":check_all_rows,
	"column": "music_ID",
	"table": "jester_music"
}

test4={
	"testname":"Check for min and max",
	"test":check_for_min_max,
	"column": "ID_auth",
	"table": "jester_users",
	"minimum":1,
	"maximum":1000
}

test5={
	"testname":"Check for min and max",
	"test":check_for_min_max,
	"column": "music_ID",
	"table": "jester_music",
	"minimum":1,
	"maximum":1000
}

test6={
	"testname":"Check for valid values",
	"test":check_for_valid_values,
	"column": "ID_auth",
	"table": "jester_users",
	"valid_values":{'100', '200', '300', '400', 'cloydvan', 'ron', 'karl', 'nadrin'}
}

test7={
	"testname":"Check for duplicates",
	"test":check_for_duplicates,
	"column": "ID_auth",
	"table": "jester_users"
}

test8={
	"testname":"Check for duplicates",
	"test":check_for_duplicates,
	"column": "music_ID",
	"table": "jester_music"
}