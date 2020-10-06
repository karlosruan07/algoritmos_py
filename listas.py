#Este programa mostra como funciona uma estrutura de uma lista, uma lista é uma varável complexa que contém várias variaveis dentro de somente uma.

frutas = ['banana','banana','abacaxi','coco','mamão']
print(frutas[2])#mostra o segundo valor da lista
frutas.append('manga')#método append adiciona um elemento no final da lista

frutas.insert(1,'abacate')#insere mais um valor do indice 1, entretanto ele não apaga o valor do indice selecionado

frutas.remove('coco')#apaga o item coco da lista

frutas.pop()#remove o ultimo valor da lista.
fruta_excluida = frutas.pop(-1)#excluiu um valor da lista e gardou esse valor.

print('A fruta excluida foi a : ', fruta_excluida)

del frutas[-1] #exclui um item permanentemente da lista
print(frutas)

print(frutas.count('banana'))#conta quantas vezes aparece o item na lista

print(sorted(frutas))#mostra a lista em ordem alfabética, ele também preserva a ordem da lista.
frutas.sort(reverse=True)#inverte a ordem da lista (de trás para frente.)

copia = frutas.copy()#copia os valores de uma lista inteira
print('Copia : ', copia)
