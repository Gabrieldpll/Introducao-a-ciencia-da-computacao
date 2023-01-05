'''
Desenvolva um código capaz de gerenciar registros de alunos de uma universidade. Cada registro é composto por quatro campos: identificador, nome, curso e idade.

Seu programa deve ser capaz de:

Ler n registros até que o usuário forneça -1
Ler n operações até que o usuário forneça -1
Realizar as seguintes operações:
Operação 1: Permitir que um aluno seja consultado por meio de seu identificador e que seu registro seja impresso caso esta operação seja selecionada
Operação 2: Permitir a consulta de todos os alunos de um determinado curso e impressão de seus registros
Operação 3: Permitir que todos os registros armazenados sejam impressos
O código deve obrigatoriamente conter:

Uma classe Aluno.
Armazenar os objetos gerados pela classe Aluno em uma lista.
Utilizar métodos do tipo get() e set() para acessar os atributos de dados do objeto.
Códigos desenvolvidos sem utilizar POO serão desconsiderados.
'''
		

class leitura:
    def __init__(self): # Nesse caso as listas são vazias , mas é possivel iniciar com lista pré-definidas passando no __init__.
        self.lista_alunos = []
        self.lista_operacoes = []
    def set_entradas_alunos(self): # essa estrutura faz uma lista até digitar -1
        recebe_dados = True
        while recebe_dados:
            x = input()
            if x != '-1':
                self.lista_alunos.append(x)
            else:
                recebe_dados = False
        return self.lista_alunos
    def set_entradas_operacoes(self): # essa a mesma coisa (Mas se executar a primeira , essa pega o segundo -1)
        dados = True
        while dados:
            y = input()
            if y != '-1':
                self.lista_operacoes.append(y)
            else:
                dados = False
        return self.lista_operacoes
    def get_alunos(self): # Metodo para conseguir a lista dos alun os que é até que o usuario digite - 1 
        lista_final = self.set_entradas_alunos() # Faz referencia ao metodo set_entradas
        return lista_final
    def get_operacoes(self):  # uma vez executado self.set_entradas_alunos o self.set_entradas_operações retorna em relação ao segundo -1
        lista_op_final =  self.set_entradas_operacoes()
        return lista_op_final


# classe de alunos depende da leitura dos dados , então ela deverá herdar 

class alunos(leitura):
    def __init__(self): 
        super().__init__() #super para herdar metodos da classe anterior
        self.lista_de_alunos = self.get_alunos() # a herança permite utilizar metodos da classe leitura
    def set_aluno(self):# como cada aluno tem 4 infomações vou cortar a lista de 4 em 4
        lista_de_alunos = [self.lista_de_alunos[i:i+4] for i in range(0,len(self.lista_de_alunos),4)]   # range(começa em 0,termina no final da lista,dando passos de 4 em 4), ou seja   l [0:4] l[4:8] l [8:12] corta em 4 pedaços
        return lista_de_alunos
    def get_lista_de_alunos(self): # metodo get para acessar oque desejamos isso cria uma estrutura lista_geral[indice do aluno][0] -> Identificador , lista_geral[indice do aluno][1] -> Nome ...... etc na ordem do problema
        return self.set_aluno()
    def print_informacoes(self,informacao): # um metodo para printar as informações dos alunos
        print('Nome: ' + str(informacao[1]))
        print('Curso: ' + str(informacao[2]))
        print('N USP: ' + str(informacao[0]))
        print('IDADE: ' + str(informacao[3]))
        print(' ')
        

# classe operação que herda a classe alunos que também herda a classe leitura

class operacoes(alunos):
    def __init__(self): 
        super().__init__() # Super para herança
        self.lista_de_operacoes = self.get_operacoes() # como visto ela herda alunos e alunos herda leitura então podemos usar metodos de leitura 
        self.lista_de_alunos = self.get_lista_de_alunos()
    def operacao_1(self): #cria o metodo das operações
        index = 0 # uma variavel acumuladora
        for j in self.lista_de_operacoes: # pecorre a lista de operações que tem estrutura fixa [operação - comando] index(comando) = index(operacao) + 1
            index = index + 1 
            if j == '1': # se ele for igual a 1 vamos executar a operação 1
                aluno = self.lista_de_operacoes[index] # armazene o seu id  consultando a lista com o index obtido 
                for h in range(len(self.lista_de_alunos)): # para quaisquer valores em nossa lista de alunos
                    if self.lista_de_alunos[h][0] == aluno: # se o valor da posicao[0] id for o mesmo que o requerido
                        informacao = self.lista_de_alunos[h]# armazene os dados desse aluno
                        self.print_informacoes(informacao) # imprima esse valor utilizando o metodo criado na classe alunos
            elif j == '2': # se a operação for do tipo 2
                curso = self.lista_de_operacoes[index] # armazene o curso
                for t in range(len(self.lista_de_alunos)):# na lista dos dados de todos os alunos vamos buscar pelo curso que esta fixo na posição 2
                    if self.lista_de_alunos[t][2] == curso:
                        informacao_2 = self.lista_de_alunos[t] # se for igual imprima suas informacoes
                        self.print_informacoes(informacao_2)
            elif j == '3': # se for 3 imprima tudo
                for c in range(len(self.lista_de_alunos)):
                    informacao_3 = self.lista_de_alunos[c]
                    self.print_informacoes(informacao_3)
                
                
                    
                
                

                    
                    
operacoes().operacao_1()  # finalmente , podemos iniciar a classe operação e aplicar o metodo operacao_1



#sobre as exigencias:
#O código deve obrigatoriamente conter:

    #Uma classe Aluno. - temos uma classe aluno
    #Armazenar os objetos gerados pela classe Aluno em uma lista. - alunos().get_lista_de_alunos() 
    #Utilizar métodos do tipo get() e set() para acessar os atributos de dados do objeto. - há vários ao longo do código.



        
  


                
         
        
        

        
