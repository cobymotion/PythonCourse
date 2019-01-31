# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:31:50 2019
Manejo de las fechas 
@author: fundacion cuervo
"""
import datetime

hoy = datetime.date.today()
print(hoy)

print('El dia es ', hoy.day)
print('El mes es ', hoy.month)
print('El año es ',hoy.year)
dias = {0:'Lunes',1:'Martes', 2:'Miercoes'}
print('El dia de la semana es ', hoy.weekday())
print(dias[hoy.weekday()])
dias_antes =datetime.timedelta(days=10)
hoy = hoy - dias_antes
fecha = datetime.date(2019,1,31)
dias = fecha - hoy 
print("Falta para la quincena " , dias.days)



