#!/usr/bin/python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="libraryproj"
#  passwd="yourpassword"
)

print(mydb)

cursor = mydb.cursor()

query = ("SELECT * from borrower")

cursor.execute(query)

for (librarycard, name, address, postalcode, phonenumber, membershipdate) in cursor:
  print("{}, {}, {}, {}, {}, {}".format(librarycard, name, address, postalcode, phonenumber, membershipdate))

cursor.close()
mydb.close()
