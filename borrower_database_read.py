#!/usr/bin/python


#The MySQL database connector for Python
import mysql.connector

#My connect string - no password - ultra high security.
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="libraryproj"
#  passwd="yourpassword"
)

#Verify that the connection string works
print(mydb)


#Cursor - not to be confused with...
#Temp space for the database query
cursor = mydb.cursor()

#My actual query string - get everything from the borrower table
query = ("SELECT * from borrower")

cursor.execute(query)

#A for loop to print out my query - computers are stupid - they only do what they're told.
for (librarycard, name, address, postalcode, phonenumber, membershipdate) in cursor:
  print("{}, {}, {}, {}, {}, {}".format(librarycard, name, address, postalcode, phonenumber, membershipdate))

#Good programming practices - no leaving connections open
cursor.close()
mydb.close()
