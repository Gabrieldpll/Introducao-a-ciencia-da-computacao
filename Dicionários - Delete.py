# -*- coding: utf-8 -*-
"""Dicionários - Delete.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jw234fae9MsmWM7g1XVwqLBi4wWxI7d5
"""
'''
Dados 3 linhas onde a primeira contem os nomes, a segunda os números de telefones respectivos. Crie uma agenda(dicionário) que relacione o Nome com seu respectivo telefone. Na terceira linha temos nomes de contatos que serão excluídos da agenda. Mostre a agenda(dicionário) resultante após as remoções.
'''
# ler dados do usuario
nomes = input().strip().split(',')
numeros = input().strip().split(',')
remover = input().strip().split(',')

#criar uma agenda usando o metodo updatate e iterando as listas (Essa função resolve esse problema , mas não resolve se tiver dados faltantes, isso é listas de tamanhos diferentes )
def criar_agenda(nomes,numeros):
  agenda = {}
  for i in range(len(nomes)):
    agenda.update({nomes[i]: int(numeros[i])})
  return agenda
# cria uma função que remove itens no dicionario conforme sua chave
def remover_contato(dicionario,itens):
  for i in itens:
    dicionario.pop(i)
  return dicionario


# Armazena no escopo global e printa o que é desejado
agenda = criar_agenda(nomes,numeros)
agenda_removida = remover_contato(agenda,remover)

print(agenda_removida)