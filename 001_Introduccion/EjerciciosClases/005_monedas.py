# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 08:59:10 2019
 Programa para nominaciones de monedas 
@author: Luis Cobian
"""
cant = int (input("Proporciona una cantidad:"))

print("La cantidad a transformar es ", cant)
"""monedas=[[500,'Billete'],[200,'Billete']
,[100,'Billete'],[50,'Billete'],[20,'Billete']
,[10,'Moneda'],[1,'Moneda']]"""
monedas = [500,200,100,50,20,10,5,2,1]
for nominacion in monedas:
    billetes = cant//nominacion
    cadena = 'Billetes' if nominacion>10 else 
    'Monedas'
    if billetes>0:
        print("{} {} de {}".format(billetes, 
              cadena, nominacion))
        cant = cant % nominacion
