class aluno:
    def __init__(self, nome, sobrenome, curso, ano):
        self.nome = nome
        self.sobrenome = sobrenome
        self.curso = curso
        self.ano = ano
        
    def mostrar(self):
        print(self.nome, self.sobrenome, self.curso, self.ano)
        
class academico(aluno): #aqui será apontada a classe que irá pegar as heranças.
    """Herança da classe pai (aluno) / Temos que colocar as informações que serão adicionadas na classe filho também."""
    
    def __init__(self, nome, sobrenome, curso, ano):
        super().__init__(nome, sobrenome, curso, ano)
        self.tcc = 'Em andamento' #é possivel também adicionar mais informações à essa classe filha.
        
    def mostrar(self):
        print(self.nome, self.sobrenome, self.curso, self.ano, self.tcc)
        
academico01 = academico(nome='Ruan - ', sobrenome='Carlos - ', curso='Redes de computadores - ', ano=2021)
        
academico01.mostrar() # é possivel também chamar uma função da classe pai.

