#Escreva um programa que lê um valor em dinheiro e calcula qual o menor número possível de cédulas de 100.00, 50.00, 10.00, 5.00 e 1.00 em que o valor lido pode ser decomposto. 
#O programa deve retornar o valor lido e a relação de notas necessárias.


# O operador // é a parte inteira da divisão. 
#Para obter o número minímo de cédulas siga a seguinte lógica :
# Começando da maior até a menor cédula comece selecionando o maior número de cédulas da cédula de maior valor em seguida subtraia o valor e repita esse procedimento para cédulas de menor valor.
# para obter a quantidade de cédulas faça dinheiro // valor da cédula
X = int(input())
cedulas_100 = X // 100    # Maior número possível de notas de 100
cedulas_50 = (X  - (100*cedulas_100)) // 50 # Já temos quantas notas de 100 então tiramos
cedulas_10 = (X  - (100*cedulas_100 + 50*cedulas_50)) // 10 # Tiramos a de 100 e 50 e assim em diante
cedulas_5 = (X  - (100*cedulas_100 + 50*cedulas_50 + 10*cedulas_10)) // 5
cedulas_1 = (X - (100*cedulas_100 + 50*cedulas_50 + 10*cedulas_10 + 5*cedulas_5)) // 1

# Printa conforme sugere a formatação da saída. 
print(str(cedulas_50) + ' de R$50,00')
print(str(cedulas_10) + ' de R$10,00') 
print(str(cedulas_5) + ' de R$5,00')
print(str(cedulas_1) + ' de R$1,00')