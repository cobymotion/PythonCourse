# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:24:12 2019

@author: Luis Cobian
Ejemplo extra 
"""
#Los dicciononarios se trabajan con llaves
diccionario = {'nombre':'Luis Cobian', 1:'prueba'}
print(diccionario) 

#agregar valor 
diccionario['telefono']='32356565'
print(diccionario) 

#obtener un valor de un diccionario 
valor = diccionario[1]; 
# valor = diccionario['no existe'] como  no se encuentra da un error
valor = diccionario.get('no existe',False)
print(valor)

#modificar un valor 
diccionario[1] = False
print(diccionario) 

#Eliminar los datos 
del diccionario[1]
print(diccionario)

#recuperar las llaves 
llaves = diccionario.keys() #objetio para iterar
print(llaves)

# como lista 
llaves = list(diccionario.keys())
print(llaves)

#obtener los valores como lista
valores = list(diccionario.values())
print(valores)

#Combinar dos diccionarios 
diccionario_2 = {'a':8712,'edad':26}
diccionario.update(diccionario_2)
print(diccionario)