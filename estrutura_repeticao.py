#Este programa mostra a maneira de como funciona uma estrutura de repetição na linguagem python.

produtos = ['Arroz', 'Feijão', 'Farinha', 'Café']

for produto in produtos:
    print(produto)

print('=_=_=_'*33)
print()

tamanho = len(produtos)
cont = 0
while cont != tamanho:
    print(produtos[cont])
    cont += 1
    
