# -*- coding: utf-8 -*-
"""subtring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DDop63vKBDNZnlUD4bJb-Qq6eV5wAn55

Desenvolva um programa que, dadas uma string (máximo 50 caracteres) e uma substring (máximo 30) fornecidas pela entrada padrão, seja capaz de identificar se a substring está contida na string.
"""

frase = str(input())
string = str(input())

if frase.find(string) != -1:
  print(f'A frase contem a substring {string}')
else:
  print(f'A frase nao contem a substring {string}')