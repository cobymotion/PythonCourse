# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:47:57 2019

@author: DevTequilaUser
"""
import datetime
import modulotec

hoy = datetime.date.today() 

modulotec.calculonomina(hoy)

ingreso = modulotec.ingresos(34,2312,1212)

print("Tu ingreso es " , ingreso)