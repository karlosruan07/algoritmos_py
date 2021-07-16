
#print(len(dicio_b)) mostra o tamanho do dicio
#dicio_b['keys_1'] = 100 #sobrescre o valor desse item
#print('keys_100' in dicio_b) verifica se a chava está contida
#dicio_b.clear() limpa a lista
#print(iter(dicio_b))
#dicio_b.pop('keys_1') remove um item

"""cont = 0
dicio_a = []
while True:
    cont += 1
    valor_stop = float(input('Digite o valor do stop em PTS : '))
    prejuizo = float(input('Digite o valor do prejuizo : '))
    gain_pts = float(input('Digite o gain em PTS : '))
    lucro = float(input('Digite o lucro : '))

    dicio_b = {'stop_pts':valor_stop, 'prejuizo':prejuizo, 'gain_pts': gain_pts, 'lucro':lucro}
    sair = str(input('Você deseja sair ? [S/N] : ')).upper()[0]
    if sair == 'S':
        break
    else:
        continue
a = 1
dicio_a[a] = dicio_b

print(dicio_a)

for k,v in dicio_b.items():
    print(f'{k} ==> {v}')"""
    
    
    
lista = ['banana', 'abacaxi', 'maçã']
print(len(lista))
