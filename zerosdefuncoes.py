# -*- coding: utf-8 -*-
"""zerosDeFuncoes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VO-AIfyJLsOI8FFUytdf9JmER7L7p_5w

**Métodos da Bissecção, Newton Raphson e Secante**
"""

import math
import sympy as sym
import sys
from sympy import *
import numpy as np


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Método da Bissecção~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bisseccao(f,a,b,epsilon):

  fa = f(a,coeficientes)
  fb = f(b,coeficientes)
  iteracoes = 100
  x = (a + b)/2
  if math.fabs(b-a) <= epsilon:
    return x
  else:
    for i in range(1, iteracoes+1):
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("Iteracao: %d" % (i))
      print("Valor de X: %f" % (x))
      print("f(x): %f" % f(x,coeficientes))
      print("epsilon: %f" % (epsilon))

      if fa * f(x,coeficientes) > 0:
        a = x
        fa = f(x,coeficientes)
      else:
        b = x
        fb = f(x,coeficientes)

      x = (a + b)/2 
      if math.fabs(b-a) <= epsilon:
        print('Valor da raiz: %f' % (x))
        return x
           
  print("O Número máximo de interações foi atingido!")
  return x1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Método de Newton Raphson~~~~~~~~~~~~~~~~~~~~~~~~~~~

def newtonRaphson(f,x0,epsilon):

  x = sym.Symbol('x')
  h = 1e-8
  #derivada = diff(f(x),x) #derivada
  iteracoes = 100
  fx0 = f(x0, coeficientes)
  if math.fabs(fx0) <= epsilon:
    return x0
 
  else:
    for i in range(1, iteracoes+1):
      derivada = (f(x0+h,coeficientes)-f(x0,coeficientes))/h
      if derivada == 0:
        print("Derivada igual a 0! Não é possível obter solução!")
      else:
        x1 = x0 - (f(x0,coeficientes)/derivada)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
        print("Iteracao: %d" % (i))
        print("Valor de X0: %f" % (x0))
        print("f(x0): %f" % (f(x0,coeficientes)))
        print("g(x): %f" % (x1))
        print("epsilon: %f" % (epsilon))

        if math.fabs(f(x1,coeficientes)) <= epsilon:
          print("\nRaíz: %f" % (x1))
          return x1
        
        x0 = x1
  print("O Número máximo de interações foi atingido!")
  return x1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Método da Secante~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def secante(f,x0, x1, epsilon):
    
  iteracoes = 100
  fx0 = f(x0, coeficientes)
  fx1 = f(x1, coeficientes)
  if abs(fx0) <= epsilon:
    return x0

  if abs(fx1) <= epsilon:
    return x1  

  for i in range(1, iteracoes+1):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
    print("Iteracao: %d" % (i))
    print("Valor de X0: %f" % (x0))
    print("f(x0): %f" % (fx0))
    print("epsilon: %f" % (epsilon))
      
    x2 = (x0*f(x1,coeficientes) - x1*f(x0,coeficientes))/(f(x1,coeficientes) - f(x0,coeficientes))
    print("g(x): %f" % (x2))  
    
    if math.fabs(f(x0,coeficientes)) <= epsilon:
      print("\nRaíz: %f" % (x2))
      return x2
      
    x0 = x1
    x1 = x2

  print("O Número máximo de interações foi atingido!")
  return x2

"""**Menu**"""

import math
import sympy as sym
from sympy import *
import numpy as np


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Coeficientes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

grau = int(input("\nInforme o grau do polinômio: "))
n = int(grau+1)
coeficientes = []
for i in range(n,0,-1):
  coeficientes.insert(0, int(input(f'\nDigite o coeficiente para o X^{i-1}:')))


#~~~~~~~~~~~~~~~~~~~~~~~~Função que gera o polinômio~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f(x,coeficientes):

  return sum(c*x**e for (e,c) in enumerate(coeficientes))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~menu~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

op = True

while op:
  while op:
    metodo = int(input('\nInforme o método que deseja utilizar:\n[1]-Bissecção\n[2]-Newton\n[3]-Secante\n[0]-Sair do programa\n'))
    if metodo == 1:
      epsilon = float(input('\nInforme o epsilon:'))
      a = float(input('\nInforme o valor a de a: '))
      b = float(input('\nInforme o valor a de b: '))
      bisseccao(f,a,b,epsilon)
      break
    if metodo == 2:
      epsilon = float(input('\nInforme o epsilon:'))
      x0 = float(input("\nInforme o valor de x0: "))
      newtonRaphson(f,x0,epsilon)
      break
    if metodo == 3:
      epsilon = float(input('\nInforme o epsilon:'))
      x0 = float(input("\nInforme o valor de x0: "))
      x1 = float(input("\nInforme o valor de x1: "))
      secante(f,x0,x1,epsilon)
      break
    if metodo == 0:
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("Programa finalizado!")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
      sys.exit(0)

    else:
      print('\n\nOpção inválida! Tente novamente.\n')

