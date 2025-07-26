#Sakila_SQL_Project

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	password='17wiknacAbc!',
	database='sakila'
)
mycursor = mydb.cursor()

mycursor.execute("Select title from film")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)
	