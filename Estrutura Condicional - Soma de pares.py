#Desenvolva um algoritmo que leia quatro números inteiros e calcule a soma dos que forem par.





numeros = []
for i in range(4):
  numero = int(input())
  numeros.append(numero)



soma = 0
for numero in numeros:
  numero = int(numero)
  if numero % 2 == 0:
    soma = soma + numero

print('A soma dos numeros pares é',soma)

