# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:13:11 2019
Ejemplos con manejo de las listas
@author: Luis Cobian 
"""

lista = ["cadenas",56,10.2,True]
print(lista)
cadenas = lista[0].upper()
print(cadenas)
print(lista[-1])
# Agrega al final 
lista.append('Final')
print(lista)
# insertar a la lista 
lista[1]=75
lista.insert(1,15)
print(lista)
# quitar un elemento de la lista
lista.remove(75)
print(lista)
# sacar valores
valor = lista.pop() 
print("El valor es {}".format(valor))
print(lista)

numeros = [65,232,65,98,65,48,5,56]
#Funcion que permite ordenar la lista m a M
numeros.sort()
print(numeros)
#Funcion que permite ordenar la lista M a m
numeros.sort(reverse=True)
print(numeros)

numeros_extra = [8,9,10]
# Concatenar las listas 
numeros = numeros + numeros_extra
print(numeros)
numeros_extra.append(numeros)
print(numeros_extra)
print(numeros_extra[3][1])

tupla = (5,'root','pass')
print(tupla)
print(tupla[1])
#tupla[1]=98
diccionario = {'user':'Luis',1001:'Administrador'}
print(diccionario)
print(diccionario.get(1001,'no existe'))

del diccionario[1001]
print(diccionario)

diccionario2 = {'server':'localhost','pass':'root'}

diccionario.update(diccionario2)
print(diccionario)
















