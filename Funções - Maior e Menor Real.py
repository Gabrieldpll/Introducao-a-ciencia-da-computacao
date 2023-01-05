'''
Desenvolva um programa que receba 10 valores reais e utilize duas funções para retornar, respectivamente, o menor e o maior deles. O uso de funções é obrigatório. Em seguida, escreva o resultado com precisão de 2 casas decimais conforme exemplo.

Entrada: 10 números reais

Saída: Duas linhas, com o menor e o maior valor dentre os 10 valores digitados respectivamente. Utilize 2 casas decimais.
'''
lista = []
for i in range(10):
    lista.append(float(input()))

def maior_numero(L,n):
  while n > 0:
    anterior = L[n-1]  
    proximo = maior_numero(L,n-1)
    if n == 1:
        proximo = anterior
        return proximo
    
    if proximo > anterior:
       return proximo
    else:
       return anterior
      


def menor_numero(L,n):
  while n > 0:
    anterior = L[n-1]  
    proximo = menor_numero(L,n-1)
    if n == 1:
        proximo = anterior
        return proximo
    
    if proximo < anterior:
       return proximo
    else:
       return anterior
      
print("%.2f" % menor_numero(lista,10))
print(maior_numero(lista,10))


