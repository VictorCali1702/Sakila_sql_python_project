#Sakila_SQL_Project

import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='17wiknacAbc!',
	database='sakila'
)
cursor = conn.cursor()
cursor.execute("select title from film limit 5")

for row in cursor.fetchall():
	print(row)
cursor.close()
conn.close()