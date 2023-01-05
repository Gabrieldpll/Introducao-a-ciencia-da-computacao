#Desenvolva um algoritmo que leia um número representando um ângulo qualquer entre 0º e 360º, calcule e escreva seu correspondente em radianos (rad = PI*angulo/180).

#Entrada: Um número real (angulo), sendo 0 <= angulo <= 360.

#Saída: Um número real representando o valor do ângulo em radianos impresso com 6 casas decimais.

import math

x = input()

try:
  x = float(x)
except:
  print("Digite um número")
  quit()

 
def converter_graus_radianos(x):
  conversão = x*math.pi/180
  return round(conversão,6)

print(converter_graus_radianos(x))