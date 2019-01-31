# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:40:26 2019

@author: Luis Cobian
"""

import pymysql #Libreria necesaria 

#Configurar los datos parta la conexion
db = pymysql.connect("127.0.0.1","root","root","snmartindb")
##################################################

# Cursor para manipular los comandos
cursor = db.cursor()

# Sentencia de SQL 
sql = "SELECT * FROM tb_asistentes"

# Execute the SQL command
cursor.execute(sql)

# Se trae los valores de 
results = cursor.fetchall()
for row in results:
   id = row[0]
   name = row[1]
   email = row[2]
   # Imprimir lo que se obtuvo
   print ("id = {0}, name = {1}, email = {1}".format(id,name,email))

# desconectar de la base de datos
db.close()