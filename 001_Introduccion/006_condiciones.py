# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:49:53 2019

@author: Luis Cobian
Practica 6
"""
#condicionante
palabra = 'works'

if palabra=='work':
    print('interno')
else:
    print('condicion falsa')

print('externo')

#otra forma
mensaje = 'esto es verdadero 'if palabra=='works' else 'esto es falso'
print(mensaje)

#mas de una condicionante
a=25
if a==1:
    print("If es {}".format(a))
elif a==2:
    pass
else: 
    print("De lo contrario ",a)
    
    