# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:25:16 2019

@author: Luis Cobian
Practica 008: Manejo de funciones 
"""

#Hacer el factorial del 4 y de 7 

#declaramos la funcion 

def factorial(numero):
    factorial = 1
    while numero>0:
        factorial = factorial * numero
        numero -=1
    return factorial 

resultado = factorial(4)
print("El resultado de 4 es ", resultado)
print("El resultado de 7 es ", factorial(7))


def funciones_multiple():
    return 3,8,"hola"

valores = funciones_multiple()

print(valores)