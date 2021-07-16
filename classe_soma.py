
#este programa tem uma classe principal que possue métodos que são importados e usados em um outro programa ao lado.

class somar:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
    def mostra_soma(self):
        print('A soma entre esses valores é : ',self.valor1 + self.valor2)
        
    def mostra_sub(self):
        print('A subtração entre esses valores é : ',self.valor1 - self.valor2)
        
    def mostra_mult(self):
        print('A multiplicação entre esses valores é : ',self.valor1 * self.valor2)
    
    
    def mostra_div_frac(self):
        try:
            print('A divisão fracionada entre esses valores é : ',self.valor1 / self.valor2)
        except:
            print('Não é possivel por zero. ')
    
        
    def mostrar_div_int(self):
        print('A divisão inteira entre esses valores é : ',self.valor1 // self.valor2)
        
    def mostrar_div_res(self):
        print('O resto da divisão entre esses valores é : ', self.valor1 % self.valor2)
        
    def mostrar_poten(self):
        print('A potencia entre esses valores é : ',self.valor1 ** self.valor2)
        
