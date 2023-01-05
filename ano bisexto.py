# -*- coding: utf-8 -*-
"""Ano bisexto

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xFGIo-ij1iL-TRmW1sHa64Pg6Lz7EZpn

Desenvolva um algoritmo que leia um ano qualquer e calcule se o mesmo é bissexto.

Dicas:

    Anos múltiplos de 4 são bissextos;  # V 
    Porém, anos múltiplos de 100 não são bissextos; # F 
    Por fim, anos múltiplos de 400 são bissextos; # V
    As últimas regras prevalecem sobre as primeiras.
    Multiplos de 100 e 4 devem retornar falso
"""

ano = int(input())

if ano % 400 == 0:
  bissexto = 'sim'
elif ano % 100 == 0:
  bissexto = 'nao'
elif ano % 4 == 0:
  bissexto = 'sim'
elif ano % 4 == 0 and ano % 100 == 0:
  bissexto = 'nao'
else:
  bissexto = 'nao'

print(bissexto)