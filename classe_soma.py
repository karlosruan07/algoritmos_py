#este programa mostra como usar uma função de soma dentro de uma classe para ser importada posteriomente.

class somar:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
    def mostra_soma(self):
        print('A soma entre esses valores é : ',self.valor1 + self.valor2)
        
    def mostra_sub(self):
        print('A subtração entre esses valores é : ',self.valor1 - self.valor2)
        
    def mostra_div_frac(self):
        print('A divisão fracionada entre esses valores é : ',self.valor1 / self.valor2)
        
    def mostra_mult(self):
        print('A multiplicação entre esses valores é : ',self.valor1 * self.valor2)
        
    def mostrar_div_int(self):
        print('A divisão inteira entre esses valores é : ',self.valor1 // self.valor2)
        
    def mostrar_div_res(self):
        print('O resto da divisão entre esses valores é : ', self.valor1 % self.valor2)
        
    def mostrar_poten(self):
        print('A potencia entre esses valores é : ',self.valor1 ** self.valor2)
        
