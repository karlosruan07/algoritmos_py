#Este programa mostra como funciona uma classe.

class aluno:
    """ TENTANDO MODULAR A CLASSE ALUNO"""
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def mostrar_aluno(self):
        print(self.nome + ' ' + self.idade)
        
aluno01 = aluno('Maria', str(9))
aluno01.mostrar_aluno()
aluno02 = aluno('João', str(10))
aluno02.mostrar_aluno()

