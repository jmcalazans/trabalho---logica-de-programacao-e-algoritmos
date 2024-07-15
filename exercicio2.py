#imprime a apresentacao da loja e o cardapio
print('--- Bem Vindo(a) a loja de Marmitas do João Márcio Calazans Britto ---\n')
print('-' * 30 + ' CARDÁPIO ' + '-' * 30 + '\n' + '-' * 70 + '\n')

def cardapio(coluna1, coluna2, coluna3): #imprime a os valores em formato de tabela
    print('--| ', coluna1, '  |  ', coluna2, '  |  ', coluna3, ' |---')

cardapio('Tamanho', 'Bife Acebolado (BA)', 'File de Frango (FF)')
cardapio('   P   ', '     R$ 16.00      ', '      R$ 15.00     ')
cardapio('   M   ', '     R$ 18.00      ', '      R$ 17.00     ')
cardapio('   G   ', '     R$ 22.00      ', '      R$ 21.00     ')

print('-' * 70)

total = 0

while True:
    while True:
        sabor = input('\nEntre com o sabor desejado (BA/FF) ou 0 para sair: ').upper() #coleta sabor do usuario e converte a entrada para maiuscula
        if sabor == '0': #verifica se a entrada e valida
            break
        elif sabor == 'BA' or sabor == 'FF':
            break
        else:
            print('Sabor inválido! Tente novamente.')
    
    if sabor == '0': #encerra o programa
        break
    
    while True:
        tamanho = input('Entre com o tamanho desejado (P/M/G) ou 0 para sair: ').upper() #coleta tamanho do usuario e converte a entrada para maiuscula 
        if tamanho == '0': #verifica se a entrada e valida
            break
        elif tamanho == 'P'or tamanho == 'M' or tamanho == 'G':
            break
        else:
            print('Tamanho inválido! Tente novamente.')
            
    if tamanho == '0': #encerra o programa
        break        

    if tamanho == 'P' and sabor == 'BA': #le as entradas e atribui valor ao pedido
        valor = 16
    elif tamanho == 'P' and sabor == 'FF':
        valor = 15
    elif tamanho == 'M' and sabor == 'BA':
        valor = 18
    elif tamanho == 'M' and sabor == 'FF':
        valor = 17
    elif tamanho == 'G' and sabor == 'BA':
        valor = 22
    else:
        valor = 21

    total += valor

    if sabor == 'BA': #imprime o que foi pedido
        saborNome = 'Bife Acebolado'
    else:
        saborNome = 'File de Frango'
    
    print(f'Você pediu um {saborNome} no tamanho {tamanho}: R$ {valor:.2f}')

    while True: #permite ao usuario adicionar ou n acressimos ao pedido
        acressimo = input('\nDeseja mais alguma coisa (S/N)? ').upper()
        if acressimo == 'S' or acressimo == 'N':
            break
        else:
            print('\nOpção Inválida!')

    if acressimo == 'N':
        break

print(f'\nO valor total a ser pago é: R$ {total:.2f}\nVolte Sempre!') #imprime total do pedido
