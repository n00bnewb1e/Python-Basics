#Day 17

#You should definitely import os module to remove any file.
import os
# os.remove("hk.txt") #If the file do not exist, you will get
# 'FileNotFoundError: [WinError 2] The system cannot find the file specified: 'jk.txt'' error

#Removing the file, skips the recycle bin. Python deletes it permanently.

if os.path.exists("bk.txt"):
    print("File exists. Removing it now")
    os.remove("bk.txt")
    print("Removed")
    
else:
    print("We cannot find the file specified")
    
# os.rmdir("abc") #rmdir() deletes the whole directory / folder
#You can only able to remove an empty directory / folder
#If you are trying to remove a directory with files in it, you will get
# 'OSError: [WinError 145] The directory is not empty: 'dirname'' error

print("################################################")

import mysql.connector #Connects python with mysql database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MyNewPass"
) #Connect to the database

print(mydb) 
print(type(mydb))

cursor = mydb.cursor() #Create a cursor first. DOn't ask me why? I don't know it yet

# cursor.execute("CREATE DATABASE dbb1") #Execute the cursor with "CREATE DATABASE DBNAME"
#If the database with name dbb1 already exists, you will get
# 'mysql.connector.errors.DatabaseError: 1007 (HY000): Can't create database 'dbb1'; database exists' error
cursor.execute("SHOW DATABASES") #Show the Database

for x in cursor: #Loop through all the databases present inside cursor
    print(x)

can = mydb.cursor()
can.execute("SHOW DATABASES")

for y in can:
    print(y)
    
print("$++++++++++++++++++++++++++++++++++++++++++")

#You can try to connect to the database while connecting .connect()

candb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MyNewPass",
    database = "dbb1"
    )

#As usual, create a cursor

akimbo = candb.cursor()
akimbo.execute("SHOW DATABASES")

for z in akimbo:
    print(x)
    
print("(((((((((((((((((((((())))))))))))))))))")