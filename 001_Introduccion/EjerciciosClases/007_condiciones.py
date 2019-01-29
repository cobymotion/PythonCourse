# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:18:22 2019
Manejo condiciones
@author: Luis CObian
"""

num = int(input('Dame un numero:'))

residuo = num%2
if residuo==0:
    print("El numero es par")    
elif num==5:
    print("El numero de la suerte es 5")
else:
    print('El numero es impar')

