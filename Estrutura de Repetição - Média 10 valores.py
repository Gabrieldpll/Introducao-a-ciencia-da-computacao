# -*- coding: utf-8 -*-
"""media de  n valores.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yrV1KQ9ImvC9eefnFe9QZck8OevUsnqW
"""

lista = list(map(int,input().split()))
n = 0
soma_dos_valores = 0
for i in lista:
  n = n + 1
  soma_dos_valores = i +soma_dos_valores

media = (soma_dos_valores/n)
print("%.2f" % media)