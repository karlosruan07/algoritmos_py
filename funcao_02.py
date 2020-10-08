#Este programa mostra como se escreve e a maneira que funciona uma função com parâmetros.

def media(media_1, media_2):
    """
    Esta função mostra a média dos parêmetros digitados.
    """
    calc = (media_1 + media_2) / 2
    print('')
    print(calc)
    print('')
    
    if(calc >= 6 and calc <=10):
        return print('Aprovado !') #se for verdade retorna essa impressão.
    elif(calc >= 4 and calc < 6):
        return print('Recuperação !')
    elif(calc >= 0 and calc < 4):
        return print('Reprovado !')
    else:
        return print('Opção inválida.')
    
media(media_1 = float(input('1ª nota : ')), media_2= float(input('2º nota : '))) #aqui são passados os parêmetros.
