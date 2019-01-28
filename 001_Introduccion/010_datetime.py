# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 02:00:18 2019

@author: coby_
Practica 10: uso de librerias  
"""

import datetime 

hoy = datetime.date.today()

print(hoy)
print("El año es ", hoy.year)
print(hoy.weekday())

dias = datetime.timedelta(days=5)

hoy_mas_cinco = hoy + dias; 

print(hoy_mas_cinco)
