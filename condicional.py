#Este programa mostra a maneira de como funciona uma estrutura de controle na linguagem python.

nota = 11

if nota >= 6 and nota <= 10:
    print('Aluno aprovado !')
elif nota >=4 and nota < 6:
    print('Aluno em recuperação !')
elif nota > 1 and nota < 4:
    print('Aluno em recuperação !')
else:
    print('Entrada inválida, digite um valor entre 0 e 10 !')