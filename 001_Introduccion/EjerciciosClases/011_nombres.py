# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:35:26 2019
Programa para agregar nombres a lista
@author: fundacion cuervo
"""
nombre = 'x'
lista=[]
while nombre!='salir':
    opcion = int(input('Opcion: '))
    if opcion==1:
        nombre = input('Dame un nombre: ')
        lista.append(nombre)
    elif opcion==2:
        print("Nombres")
        print(lista)
    elif opcion==3:
        print("Nombres")
        print(lista[::-1])
    elif opcion==4:
        break
    else:
        print("Opcion no valida")


