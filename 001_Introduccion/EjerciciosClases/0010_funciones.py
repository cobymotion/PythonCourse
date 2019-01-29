# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:45:37 2019
Manejo de funciones 
@author: Luis Cobian
"""

def saludo():
    print("Ya casi nos vamos")
    print("No desesperen")

def suma(a,b):
    r = a +b 
    print("El resultado es ", r)

def sumaRetorno(a,b):
    r = a +b 
    return r,a,b

   
print("asasdad")
saludo()
print("Pero")
saludo()
suma(5,7)
resultado = sumaRetorno(4,2)
print(resultado[0])



