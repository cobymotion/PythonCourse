# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:41:16 2019

@author: Luis Cobian
Practia 4: listas
"""
mi_lista = ["cadenas",16,65.2,True]
print(mi_lista)
# Agregar valores a la lista 
mi_lista.append(7)
print(mi_lista)
#Inserta valor a la lista 
mi_lista.insert(2,"Insertado")
print(mi_lista)
#Remover un valor
mi_lista.remove(16)
print(mi_lista)
#Pueden trabajar como pilas 
valor = mi_lista.pop()
print(valor)
print (mi_lista)

#ordenando listas
#mi_lista.sort(); # no es posible ya que no tienen los mismos datos

mi_lista_enteros = [5,9,10,3,5,4,3]
mi_lista_enteros.sort(); 
print(mi_lista_enteros);
# En orden inverso 
mi_lista_enteros.sort(reverse=True)
print(mi_lista_enteros);
# unir dos listas 
mi_lista_dos = [4,3,2]
mi_lista_enteros = mi_lista_enteros + mi_lista_dos
print(mi_lista_enteros);
# añadir una lista dentro de otra
mi_lista_enteros.append(mi_lista_dos)
print(mi_lista_enteros)
print(mi_lista_enteros[10])
print(mi_lista_enteros[10][1])
