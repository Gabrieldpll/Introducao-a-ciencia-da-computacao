"""
Faça um programa que dado um intervalo dado por dois numeros X e Y, imprima todos os primos.

Entrada: Intervalo

Saída: Os primos nesse intervalo
"""
X , Y = input('').split()
X = int(X)
Y = int(Y)

# Função divisor
def divisores(numero):
  lista_de_divisores = []
  for i in range(1,numero+1):
    if numero % i == 0:
      lista_de_divisores.append(numero//i)
  return(lista_de_divisores)
# um numero é primo se ele é divisivel por 1 e ele mesmo
for j in range(X,Y+1):
  if divisores(j) == [j,1]:
    print(j)
    
