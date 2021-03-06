# -*- coding: utf-8 -*-
"""MetodoEulerAperfeicoado

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DEXymWiD1PbVOr-IY7mBs3RhKMQk40GM
"""

from scipy.integrate import quad
import math
import numpy as np
from scipy.integrate import quad


def f(x, y):
    return  4 - 2*x

#formula do Método de Euler aperfeiçoado
#y1 = y0 + 1/2*(k1+k2)*h
#y0 = f(x0)
def metodoheun(h, n, x0, y0):

  x = x0
  y = y0
  for i in range (n):
    k1 = f(x, y)
    k2 = f(x + h, y + (h*k1))
    y = (y + (h/2)*(k1 + k2))
    x = x + h
    print(i,k1,k2)
    print(f"iteração:{i}\nyi = {y} + 0.25[{k1} + {k2}]")
    
  return y
      
resultHeun = metodoheun(0.5, 10, 0, 2)
print("Método de Euler aperfeiçoado:", resultHeun, "\n")

import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return  -x/y

def rk4(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = h*f(x[k], y[k])
        m2 = h*f(x[k] + h / 2, y[k] + m1/2)
        m3 = h*f(x[k] + h / 2, y[k] + m2/2)
        m4 = h*f(x[k] + h, y[k] + m3)
        y[k + 1] = y[k] + (1/ 6) * (m1 + 2 * m2 + 2 * m3 + m4) # <- fórmula do método de Runge-Kutta
        print("\nm1:", m1)
        print("\nm2:", m2)
        print("\nm3:", m3)
        print("\nm4:", m4)
        print("\ny:", y)
    return x, y

met = rk4(f, 0, 20, 4, 5)
print(met)