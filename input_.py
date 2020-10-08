#Este programa mostra a maneira que um programa tem uma interação por meio do teclado.

nota_1 = float(input('Dogite a 1ª nota : '))
nota_2 = float(input('Digite a 2ª nota : '))

media = (nota_1 + nota_2) / 2
print('')
print(media)

if(media >=6 and media <=10):
    print('Este aluno foi aprovado !')
    
elif (media >=4 and media < 6):
        print('Este aluno está em recuperação !')

elif (media >= 0 and media < 4):
    print('Este aluno está reprovado !')
    
else:
    print('Opção inválida ! Digite uma nota entre 0 e 10 : ')
        
