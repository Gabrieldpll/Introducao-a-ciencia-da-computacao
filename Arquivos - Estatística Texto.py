'''
Faça um programa em Python que leia o arquivo de texto chamado dados.txt e guarde o seu conteúdo em umaclasse. Esse arquivo contém o primeiro nome de uma pessoa, o seu sexo e por último a idade. O seu programa deverá ler esse arquivo, calcular e então imprimir quantos registros tem no total, a quantidade de homens, a quantidade de mulheres, a média de idade total, a média de idade dos homens e por fim, a média de idade das mulheres. Use duas casas decimais para imprimir as médias de idade.
'''

class Pessoa(object):
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo


lista = []

with open('dados.txt') as dado:
    for linha in dado:
        linha = linha.split()
        objeto = Pessoa(linha[0],linha[2],linha[1])
        lista.append(objeto)

        
registros = 0
muie = 0
homi = 0
idade_muie = 0
idade_homi = 0
idade_total = 0

for objeto in lista:
    registros += 1
    idade_total += objeto.idade
    if objeto.sexo == 'f':
        muie += 1
        idade_muie += objeto.idade
    else:
        homi += 1
        idade_homi += objeto.idade

print(f"{registros} {homi} {muie} {idade_total/registros:.2f} {idade_homi/homi:.2f} {idade_muie/muie:.2f}")
