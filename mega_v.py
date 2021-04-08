
from random import choice
numeros = [10,27, 40,46,49,58,2, 10, 34, 37, 43, 50, 3, 4, 29, 36, 45, 55, 14, 32, 33, 36, 41, 52, 20, 30, 36, 38, 47, 53,
           1, 5, 11, 16, 20, 56, 2, 18, 31, 42, 51, 56, 5,  11,  22, 24, 51,  53, 6, 37, 34, 10, 3, 17, 5, 10, 12, 18, 25, 33,
           3,  35,  38,  40,  57,  58]
lista_repete = []
lista_nao_repete = []

for c in range(1,61):
    quant_nuum =  numeros.count(c)
    if quant_nuum >= 3 and quant_nuum <=4:
        lista_repete.append(c)
    elif quant_nuum < 3:
        lista_nao_repete.append(c)
        #print('')
        #print(f'O número {c} apareceu {quant_nuum} vezes na lista.')
        
for c3 in range(1,3):
    lista_repete.append(choice(numeros))

        
        
print('')
print('===============  ORDEM SORTEADA ! ====================')
for repete in lista_repete:
    print(f'==> {repete}')
print('')
"""print('===============  REPETIU 2 VEZES ! ====================')
for nao_repete in lista_nao_repete:
    print(f'==> {nao_repete}')"""
