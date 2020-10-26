#este programa mostra o uso de importação de classes;

import sqlite3
from sqlite3 import Error

class hospital:
    def __init__(self, nome, tipo, especialidade, avaliacao):
        self.nome = nome
        self.tipo = tipo
        self.especialidade = especialidade
        self.avaliacao = avaliacao
        
    def inserir(self):
        
        try:
            conecta = sqlite3.connect('C:\\Users\Ruan\Documents\curso_ifto\python_algoritmos\hospitalar1') #C:\Users\Ruan\Documents\curso_ifto\python_algoritmos  C:\hospitalar1
            cursor = conecta.cursor()
            """
            docstring
            """
            while True:
                self.nome = input('Digite seu nome : ')
                self.tipo = input('Digite o tipo de hospital : ')
                self.especialidade = input('Digite a especialidade : ')
                self.avaliacao = input('Qual a sua avaliação : ')
                
            
                cursor.execute("""INSERT INTO hospital(nome_hosp,tipo_hosp,especia_hosp,avalia_hosp)
                            VALUES(?,?,?,?)
                """, (self.nome, self.tipo, self.especialidade, self.avaliacao))
            
                conecta.commit()
                sair = str(input('Você deseja sair ? [S/N] : ')).upper()[0]
                if sair == 'N':
                    break
                else:
                    continue
        except Error as e:
            print(e)
        
    def mostrar(self):
        try:
            conecta = sqlite3.connect('C:\\Users\Ruan\Documents\curso_ifto\python_algoritmos\hospitalar1')
            cursor = conecta.cursor()
            cursor.execute("SELECT * FROM hospital")
            for linha in cursor:
                print(linha)
        except Error as e:
            print(e)
        