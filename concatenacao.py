#este programa mostra a maneira de como concatenar e combinar string.

nome = 'Ruan'
segundo_nome = 'carlos'
terceiro_nome = 'tavares'

print(nome + ' '+ segundo_nome + ' '+ terceiro_nome) #concatena (junta) string
print('Seu nome é : '+ nome + " " + segundo_nome +' '+ terceiro_nome) #combiando com textos
print('\t Seu nome é : '+ nome + " " + segundo_nome +' '+ terceiro_nome) #tabulando textos
print('Seu nome é : \n'+ nome + " " + segundo_nome +' '+ terceiro_nome) # quebra de linha

print('=-='*30)

nome2 = ' Maria '
segundo_nome2 = ' lucineide '
terceiro_nome2 = ' Da silva '

print(nome2.lstrip()) #remove os espaços em branco da esquerda
print(segundo_nome2.rstrip()) #remove os espaços em branco da direita
print(terceiro_nome2.strip()) #remove os espaços em branco dos dois lados.

print('=-='*30)