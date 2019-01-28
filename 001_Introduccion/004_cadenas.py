# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:23:59 2019

@author: DevTequilaUser
Practica 3: Cadenas
"""

nombre = "Luis Cobian"
print(nombre)
mi_bio = """INSTITUTO TECNOLOGICO 
DOCENTE PTC
INFORMATICA"""

print(mi_bio)

#Formas de concatenar cadenas
cade1 = "cadena"
cade2 = 'xxxxxx'
#Primera forma
unidos = "Esta es la primera cadena '" + cade1 + "' y la otra es '" + cade2 + "'"
print(unidos)
#Segunda Forma
unidos ="Esta es la primera cadena '%s' y la segunda es '%s'" %(cade1,cade2)
print(unidos)
#Tercera forma
unidos = "Esta es la primera cadena '{}' y la segudnda es '{}'" . format(cade1,cade2)
print(unidos)

#Obtener un caracter 
print(nombre[-1]) #Ultimo caracter 
print(nombre[0]) #Primer caracter
print(nombre[3:8]) # Del 3 al 4 
print(nombre[:8]) # ???????
print(nombre[3:]) # ??????
print(nombre[:8:2]) #??????
print(nombre[::-1]) # ???????

espacio = '''
'''
new_bio = mi_bio.replace(espacio,'')
print (new_bio)