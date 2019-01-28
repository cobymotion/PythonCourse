# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:15:33 2019

@author: Luis Cobian
Practica: 007 ciclos While
"""
#
contador =0 
while contador<=10:
    print("Es una prueba " ,contador)
    contador+=1
    if contador == 5:
        continue;
    elif contador==8:
        break;
    print("vuelta")
#else:
 #   contador=3    
print("termino el programa " ,contador)