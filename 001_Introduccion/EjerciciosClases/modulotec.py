# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:16:54 2019
Algunas operaciones 
@author: Luis Cobian
"""
import datetime 

def datosautor():
    print("Luis Cobian")
    print("Informatica")
    
def fechapagonomina(fecha):
    mes = fecha.month
    year = fecha.year
    if fecha.day>15:
        if mes==12:
            mes=1
            year+=1
        else:
            mes+=1
        quincena=datetime.date(year,mes,1)
        quincena=quincena - datetime.timedelta(days=1)
    else:
        quincena = datetime.date(year,mes,15)
    ajuste = 7 - quincena.weekday()
    if ajuste <=2:
        quincena = quincena + \
        datetime.timedelta(days=ajuste)
    dias = quincena-fecha
    print("Faltan {} dias para la quincena"
          .format(dias.days))
    print("Fecha estimada para quinena "\
          ,quincena)
                              
    
def calculoImpuesto(cantidad):
    """
    Funcion que dependiendo la cantidad
    te calcula el 32% 
    lleva una cantidad como param
    retorna un cantidad con el impuesto 
    """
    impuesto = cantidad * 0.32
    return impuesto

def sumaIngresos(*ingresos):
    suma = 0
    for ingrero in ingresos:
        suma+=ingrero
    return suma












