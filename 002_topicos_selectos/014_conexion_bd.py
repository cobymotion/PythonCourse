# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:40:26 2019

@author: DevTequilaUser
"""

import pymysql

############### CONFIGURAR ESTO ###################
# Open database connection
db = pymysql.connect("127.0.0.1","root","root","snmartindb")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to READ a record into the database.
sql = "SELECT * FROM tb_clientes"

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
   id = row[0]
   name = row[1]
   email = row[2]
   # Now print fetched result
   print ("id = {0}, name = {1}, email = {1}".format(id,name,email))

# disconnect from server
db.close()