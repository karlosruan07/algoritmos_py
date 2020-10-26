#definições de um computador;

#computador = marca, placa de vídeo, Quant_ra, HD

class computador:
    def __init__(self, marca, memoria_ram, placa_de_video, hd):
        """
        docstring
        """
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.hd = hd
        
    def ligar(self):
        print('Estou ligando')
    def desligar(self):
        print('Esou desligando')
    def exibir_info(self):
        print(self.marca, self.placa_de_video, self.hd)

computador1 = computador('Samsung', '8 GB', 'Nvidia', '480 GB')

computador1.ligar()
computador1.desligar()
computador1.exibir_info()

#marca, memo_ram, hd
class computador:
    def __init__(self, marca, memoria_ram, hd):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.hd = hd
        
    def exibir_info(self):
        print(self.marca, self.memoria_ram, self.hd)
        
computador1 = computador('Samsung', '8 GB', '480 GB')

computador1.exibir_info()
















        





















