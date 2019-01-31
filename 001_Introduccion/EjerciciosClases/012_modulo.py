# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:26:39 2019
Llamando a un modulo 
@author: Luis Cobian
"""
import datetime
import modulotec as c

c.datosautor()
i = c.calculoImpuesto(1000)
print(i)

res = c.sumaIngresos(56,873,542,542,12)
print(res)

fecha = datetime.date(2019,6,24)
c.fechapagonomina(fecha)


