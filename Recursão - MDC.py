# -*- coding: utf-8 -*-
"""Recursão - MDC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17L7ihlm0kLxZ3jGAwOL42uNypnemA40w
"""

x = int(input())
y = int(input())

def mdc(a,b):                      # algoritmo de euclides .  nele a > b (esperamos que o usuario saiba , mas caso contrario resolvi fazer um if)
  if b > a:                 
    a,b = b,a
  if b == 0:                   # condição de parada o resto é 0
    return a 
  else:  
    return mdc(b, a%b)         # se  o resto não for 0 execute mdc(menor,resto)   

print(mdc(x,y))