# -*- coding: utf-8 -*-
"""lagrange

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GyQ6-W_7pRuuvZXdGZQJIK_MSqXQorby
"""

import numpy as np


x = np.array([-1, 0, 2])
y = np.array([4, 1, -1])

n = len(x)

#grau = float(input('Informe o grau do polinômio interpolador:\n'))

escolha = int(input("Escolha qual método deseja utilizar: \n1 - Interpolação de Lagrange \n2 - Interpolação de Newton\n"))

#pontoespec = float(input('Caso deseja calcular algum ponto específico, informe:\nSe NÃO deseja calcular algum ponto específico aperte ENTER\n'))

if escolha == 1:
  
  def lagrange(x,y,p):

    for k in range(0, n, 1):
      numerador = 1
      denominador = 1 
      

    for j in range(0, n, 1):

      if k != j:
        numerador = numerador * (x - x[j])
        denominador = denominador * (x[j] - x[k])

      p = p + y[k]*(numerador/denominador)
        
    print(p)

if escolha == 2:

  def newton(x,y,p):
    p = 0
    for i in range(0, n, 1):
      fy[i] = y[i]

    for k in range(0,n-1,1):
      for i in range(n, k+1, -1):
        fy[i] = (fy[i] - fy[i-1])/(x[i] - x[i-k])
    
    

    for i in range(n-1, 0, -1):
      fy[i] = fy[i]*(x - x[i]) + fy[i]

    print(p)

if escolha != 1 and escolha !=2: 
  print('Escolha inválida!')