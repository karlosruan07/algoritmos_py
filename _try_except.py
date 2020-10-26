#Este programa mostra como funciona o mod0 try e except, o método serve para não parar a execução de um programa.

def divisor_zero(numero):
    """
    O número que for igual a zero como parâmetro não irá continuar a execução
    """
    try:
        divisao = 50 / numero
        return print(divisao)
    
    except:
        print('Não é possível dividir por zero.')#Essa linha será executada se caso for dividido por zero. Depois daqui, a execução não volta para o bloco Try.
    
divisor_zero(0)
