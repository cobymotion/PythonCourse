# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:42:09 2019
Pruebas con cadenas 
@author: Luis Cobian
"""
nombre = "Luis Cobian"
print(nombre) 
biografia = """Docente del tec
Estudio algo
y hago alggo"""

print(biografia)
print("----------------")
cv = "Nombre " + nombre + "\n" + biografia

print(cv)
print("----------------")
cad1 = "Hola " 
cad2 = "como estas"
#Otra forma de concatenar cade
unidas = "Es %s un saludo,¿ %s ?" %(cad1,cad2) 
print(unidas)
# Tercera forma
unidas = "La c1 {} y la c2 {}".format(cad1,cad2)
print(unidas)

print(unidas[0])
print(unidas[3]) 
print(unidas[-1])
print(unidas[5:8])
print(unidas[:10])
print(unidas[3:])
print(unidas[6::2])
print(unidas[::-1])







