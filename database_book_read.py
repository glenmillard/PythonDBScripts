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

query = ("SELECT * from book")

cursor.execute(query)

for (title, author, cost, isbn_number) in cursor:
  print("{}, {}, {}, {}".format(title, author, cost, isbn_number))

cursor.close()
mydb.close()
