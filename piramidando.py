#Este programa mostra como piramidar na bolsa de valores.


def calc():
    """
    Esta função calcula toda a operação.
    """
    lista_entradas = []
    lista_dados = []
    lista_copia = []
    while True:
        quant_contratos = int(input('Com quantos contratos vai operar ? : '))

        posi_piramide = int(input('Qual a posição da pirâmide ? : '))
        
        
        entrada = float(input('Digite a entrada na operação : '))
        lista_entradas.append(entrada)
        
        stop_loss = float(input('Digite o stop loss da operação : '))
        
        loss = entrada - stop_loss
        #print('O loss dessa operação é de ',loss,'pts.')

        stop_gain = float(input('Digite o alvo da operação : '))
        
        
        
            #apagar esse for
        quant_intens = 0
        for itens in lista_entradas:
            quant_intens += 1
                
        preco_medio = sum(lista_entradas)/ len(lista_entradas)
        #print('O preço médio de todas as entradas é de ',preco_medio,'.')
            
        stop_pts = stop_loss - preco_medio
            
        #print('O stop de Pts é de ',stop_pts,'Pts.')
            
        prejuizo = stop_pts * quant_contratos * posi_piramide * preco_ativo
            
        #print('O prejuizo dessa operação é de ', prejuizo,'R$')
            
        gain_pts = stop_gain - preco_medio
            
        #print('Nessa operação você irá ganhar ', gain_pts,'Pts.')
            
        lucro = gain_pts * quant_contratos * posi_piramide * preco_ativo
            
        #print('Com essa operação você terá ', lucro,'R$ de lucro')
            
        dicio = {'stop_pts': stop_pts, 'prejuizo R$':prejuizo, 'gain_pts': gain_pts, 'lucro R$':lucro}
            
        #for k,v in dicio.items():
            #print(f'{k} ==> {v}.')
            
            
        lista_dados.append(dicio)
        for lista in lista_dados:
            print('=_=_='*10)
            for k,v in dicio.items():
                print(f'{k} ==> {v}.')
        #print('=_=_='*10)
        lista_dados.clear()
            
            
        sair2 = str(input('Você deseja sair ? [S/N] : ')).upper()[0]
        if sair2 == 'S':
            break
        else:
            continue
    
while True:
    print('')
    print("1 - Mini-indice;\n2 - Mini dolar.")
    opcao_ativo = str(input('Qual ativo você irá operar ? Escolha sua opção : ')).upper()[0]
    print('')
    while opcao_ativo not in '12':
        opcao_ativo = str(input('Qual ativo você irá operar ? Escolha sua opção : ')).upper()[0]
    
    if opcao_ativo == '1':
        preco_ativo = 0.20
        print('Você vai operar Mini-indice !')
        print('')
        
        calc()
        
    else:
        preco_ativo = 10
        print('Você vai operar mini-dolar !')
        
        calc()
        print('')
        
    
    sair = str(input('Você deseja sair ? [S/N] : ')).upper()[0]
    if sair == 'S':
        break
    else:
        continue
    
