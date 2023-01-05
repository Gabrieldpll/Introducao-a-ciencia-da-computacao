'''
Escreva um programa que recebe 3 lados de um triangulo e retorna se o triangulo é isósceles (dois lados iguais), escaleno (todos os lados diferentes) ou equilátero (todos os lados iguais).

Entrada: Três números reais

Saída: Uma mensagem de "isosceles", "escaleno" ou "equilatero".

'''

# lendo dados
x, y, z = input().split(' ')
x = float(x)
y = float(y)
z = float(z)
# se todos lados sao iguais ele é equilatero
if x == y and x == z:
  print('equilatero')
elif (x==y) or (x==z) or (y==z):  # Se alguma dupla de lados são iguais ele é isosceles
  print('isosceles')
else:  # Se não sou todos iguai , ou dois a dois iguais,eles são todos difernetes,i.e escaleno
  print('escaleno')
