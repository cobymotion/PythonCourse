# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:33:54 2019
Programa que permite contar 
las vocales dentro de una palabra
@author: Luis Cobian
"""

palabra = input("Una palabra: ")
palabra = palabra.lower(); 
a = palabra.count("a");
e = palabra.count("e");
i = palabra.count("i");
o = palabra.count("o");
u = palabra.count("u");

print("A: ",  a)
print("E: ",  e)
print("I: ",  i)
print("O: ",  o)
print("U: ",  u)












