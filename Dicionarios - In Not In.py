# -*- coding: utf-8 -*-
"""Dicionarios - In Not In.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FOND5tXXZgq7GFuJN6FY2_NoP_hYsyzT
"""

		

'''
Dados 3 linhas onde a primeira linha temos os nomes do correntistas, na segunda seus respectivos saldos. Monte um dicionario vinculando a pessoa com seu saldo atual. Na terceira linha temos alguns nomes de clientes que serão pesquisados pelo gerente, caso o nome seja de um cliente cadastrado mostre seu saldo caso contrário mostre "Nao Cadastrado" na tela.
'''

nomes = input().split(',')
saldo = input().split(',')
lista_contatos = input().split(',')
h = dict()
for i in range(len(nomes)): 
  h.update({nomes[i]:saldo[i]})

for j in lista_contatos:
  if j in nomes:
    print(h.get(j))
  else:
    print('Nao Cadastrado')