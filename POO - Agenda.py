'''
Implemente uma agenda com data, hora e atividade a ser realizada, em que data contém, dia, mês e ano e hora contém hora, minuto e segundo. Será passado a quantidade de atividades seguida da data da hora e da atividade. As entradas e saídas deverão ser exibidas de acordo com o exemplo a seguir:

O programa deve conter:

Uma classe Agenda.
Uma classe Data.
Uma classe Hora.
Métodos do tipo get() e set() para acessar atributos de dados.
'''






N = int(input()) # recebe o numero de agendas
class agenda: # uma classe que cria nossas agendas
    def __init__(self,lista): # inicia o programa uma lista que será atualizada posteriormente
        self.lista = lista
    def SetAgenda(self):  # esse metodo atualiza a lista que iniciamos com os inputs
        ac = 0
        while ac < 7:   # como há 7 entradas fazemos um while com o truque da variavel acumuladora
            self.lista.append(input()) # o usuario digita algo e isso é armazenado na lista
            ac = ac + 1
        return self.lista # retorna a lista
    def GetAgenda(self): # um metodo para conseguir a agenda
        lista_atualizada = self.SetAgenda() # chama o metodo anterior pelo self.Setagenda() armazena localmente seu resultado e em seguida o retorna
        return lista_atualizada



# Nossa estrutura de dados é fixa isso é dia é a primeira posição , mes a segunda e ano a terceira . Assim podemos criar uma função que transforma isso em data
class data: 
    def __init__(self,lista):
        self.lista = lista # inicia com uma agenda(no caso criada em uma lista)
    def SetData(self): # utiliza a estrutura fixa e retorna uma lista [ data , mes , ano ]
        dia = self.lista[0]
        mes = self.lista[1]
        ano = self.lista[2]
        return dia,mes,ano
    def GetData(self):# Chama o metodo que retorna dia , mes , ano e o formata utilizando desempacotamento de listas
        data = self.SetData() 
        return "{}/{}/{}".format(*data)

# a mesma ideia di anterior 
class horas: 
    def __init__(self,lista):
        self.lista = lista
    def SetHoras(self):
        hora = self.lista[3]
        minuto = self.lista[4]
        segundo = self.lista[5]
        return hora,minuto,segundo
    def GetHoras(self):
        horas = self.SetHoras()
        return "{}:{}:{}".format(*horas)


# Como eles nos forneceu N agenda faremos um for para executar essas N agendas        
        
for i in range(N):
    agenda_completa = agenda([]).GetAgenda() # isso retorna uma lista com nossa agenda comple
    d= data(agenda_completa)   #  inicia as classes datga e horas com a agenda
    h = horas(agenda_completa) #  
    print('{} - {}'.format(d.GetData() ,h.GetHoras())) # usa  os metodos get_data e get_horas que retornam data e horas formatados e os printas no formato data - hora 
    print(agenda_completa[-1]) # Retorna a mensagem , no caso a ultima posicao da lista
 
 


    
    
