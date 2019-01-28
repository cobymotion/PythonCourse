# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:10:24 2019

@author: Luis Cobian
Practica 008 Variables globales
 
"""


def palindromo() :
    global frase
    cadena_sin_espacios = frase.replace(' ','') #variables locales   
    frase = 'Limpiada'
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

frase = 'anita lava la tina' #variables globales
resultado = palindromo()
print (frase)
print(resultado)

