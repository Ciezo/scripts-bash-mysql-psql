#!/bin/sh 

# Author: Cloyd Van S. Secuya
# Filename: createdb_local.sh
# Date of Creation: July 13, 2022 
# Description: 
#       A script that can automate the creation of a database schema 
#       with initialized default values on the localhost. 

# Credentials 
# NOTE: Change these based on your own setup MySQL server on localhost!
user="root"
pass="cloyd27feb2002"       

echo "Connecting to localhost machine..."
# NOTE: Uncomment this if interactive mode is wanted!
# mysql -h "localhost" -u "root" "-pcloyd27feb2002" -P 3306

echo "Creating and loading up schema!"
cat "../mysql/jester_sc.sql" | mysql -u root -p; 

echo "Loading up areas for staging!"
mysql -h "localhost" -u "$user" "-p$pass" "Jester_DB" < "popu_jester_users-tbl.sql";
mysql -h "localhost" -u "$user" "-p$pass" "Jester_DB" < "popu_jester_music-tbl.sql";

echo "Viewing available databases on localhost"
# mysql -u root -p -h 127.0.0.1 -P 3306 -e "show databases";
mysql -h "localhost" -u "$user" "-p$pass" -e "show databases";
echo "Available databases returned!"