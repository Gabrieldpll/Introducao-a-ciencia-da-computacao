'''
Escreva um programa que recebe 3 valores e escreva os valores em ordem crescente.

Entrada: Três números inteiros

Saida: Os três númeors inteiros ordenados de forma crescente.
'''
x, y, z = input().split(' ')
x = int(x)
y = int(y)
z = int(z)

# x é o maior
if x < y and x < z:
  if y < z:
    print(x,y,z)
  else:
    print(x,z,y)

# y é o maior 

if y < x and y < z:
  if x < z:
    print(y,x,z)
  else:
    print(y,z,x)

# z é o maior
if z < x and z < y:
  if x < y:
    print(z,x,y)
  else:
    print(z,y,x)
