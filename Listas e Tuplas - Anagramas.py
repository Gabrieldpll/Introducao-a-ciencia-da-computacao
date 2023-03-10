# -*- coding: utf-8 -*-
"""anagrama_corrigido.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OHFQwRsQpNoaYKT12L-qVHDTbDaVYoWt
"""
'''
Dadas N strings, determinar quantos anagramas existem para cada uma.

Entrada: Um inteiro positivo N; em seguida, N linhas, cada uma contendo uma string de carácteres alfabéticos minúsculos, seguidas de uma quebra de linha (‘\n’)

Saída: N linhas, cada uma contendo um inteiro que representa a quantidade de anagramas; a i-ésima linha impressa é a resposta para a i-ésima string inserida, com i de 1 até n.
'''
# dados do usuario 
lista_de_palavras = []
num_linhas = int(input())
for l in range(num_linhas):
  lista_de_palavras.append(str(input()).rstrip())

# Uma função para o fatorial
def fatorial(n):          # já foi feito 
  if n == 0 or n == 1:
    return 1
  else:
    return n*fatorial(n-1)

# uma função que nos fornce os anagrmas com variaveis locais
def anagrama(string):
  elementos_diferentes = []
  repeticoes = []
  denominador = 1
  for i in string:
    if i not in elementos_diferentes:     # se uma letra da string nao esta na lista agregue na lista de diferentes
      elementos_diferentes.append(i)
  for j in elementos_diferentes:             # para cada elemento diferente veja quantas vezes eles repete
    repeticoes.append(string.count(j))
  for h in repeticoes:                       # para cada repetição aplique o fatorial e multiplique pela proxima
    denominador = denominador* fatorial(int(h))
  print(int((fatorial(len(string))/ denominador)))      # formula do anagrama e já os printa


for palavras in lista_de_palavras:
  anagrama(palavras)