#Este programa mostra como funciona uma estrutura de uma lista, uma lista é uma varável complexa que contém várias variaveis dentro de somente uma.


frutas = ['banana','banana','abacaxi','coco','mamão']

print('Lista original : ', frutas)
print('')
print('lista em ordem alfabética : ', sorted(frutas)) #o método sorted preserva a ordem da lista.
frutas.reverse()
print('ordem reversa : ',frutas)
frutas.reverse()#volta ao valor original
print('Ordem ORIGINAL : ',frutas)

print('Essa lista tem o tamanho de : ', len(frutas))#retorna o tamanho da lista
