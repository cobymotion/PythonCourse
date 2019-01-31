# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:56:37 2019
Manejo de ciclos 
@author: Luis Cobian 
"""
contador = 0 

while contador<=10:
    if contador%3==0 and contador!=0:
        contador+=1
        continue
    elif contador==7:
        break
    print (contador)
    contador+=1
else:
    print ("Fin del ciclo normal")

print("Ejemplo de FOR")

lista = [1,2,3,5,6,8,7]

for elemento in lista:
    print(elemento)
print("-------------------------")
for i in range(0,10,2):
    print(i)

for indice,valor in enumerate(lista):
    print("{} El valor es {}".format(indice,valor))












