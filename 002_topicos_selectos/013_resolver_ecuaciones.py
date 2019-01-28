# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:05:11 2019

@author: Luis Cobian
"""

import numpy as np

A = np.array([[1, 2, 3],
              [2, 5, 2],
              [6, -3, 1]])

A = np.array([[1, 2, 3],
              [2, 5, 2],
              [6, -3, 1]])

b = np.array([6, 4, 2])

x = np.linalg.solve(A, b)

print(x)


