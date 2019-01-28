# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 07:57:01 2019

@author: coby_
Practica 011: Repositorios
https://pypi.org/project/googletrans/ 
"""

from googletrans import Translator
translator = Translator()
print(translator.translate('how are you?', dest='es',src='en'))
