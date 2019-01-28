# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:24:34 2019

@author: Luis Cobian 
Practica: 007 Ciclos FOR
"""
lista = [3,56,2,23,1,6,43,2,31,23]
#iterando una lista de valores 
for valor in lista: 
    print(valor)

print("-----------------------")  
nueva_lista = range(5,20,3)
for valor in nueva_lista:
    print(valor)

print(nueva_lista)

#uso de enumerate 
for indice, valor in enumerate(nueva_lista):
    print(valor, " tiene el indice ", indice)
    
print("Numero de elementos ", len(lista))
#Recorrer un diccionario
diccionario = {'nombre':'Luis Cobian', 1:'prueba'}
for llave,valor in diccionario.items():
    print(llave, " => ", valor)

#Otra forma 
for llave,valor in diccionario.items():
    print(f"{llave} => {valor}")
        
for i in range(10):
    print(i)
    
#python comprenhesion 
lista = [valor for valor in range(101)]
print(lista)