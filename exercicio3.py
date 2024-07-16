# Mensagem de boas vindas
print('Bem vindos a Fábrica de Camisetas do João Márcio Calazans Britto\n')

def escolha_modelo(): # funcao para escolha do modelo de camiseta
    while True:
        print('\nEscolha o modelo desejado:')
        print('MCS - Manga Curta Simples')
        print('MLS - Manga Longa Simples')
        print('MCE - Manga Curta Com Estampa')
        print('MLE - Manga Longa Com Estampa')
        modelo = input('Digite o código do modelo: ').upper() #recebe a entrada, converte para maiusculo e verifica se e um valor valido
        if modelo == 'MCS':
            return 'Manga Curta Simples', 1.80
        elif modelo == 'MLS':
            return 'Manga Longa Simples', 2.10
        elif modelo == 'MCE':
            return 'Manga Curta Com Estampa', 2.90
        elif modelo == 'MLE':
            return 'Manga Longa Com Estampa', 3.20
        else:
            print('Modelo inválido. Tente novamente.')

def num_camisetas(): 
    while True:
        try:
            num = int(input('\nDigite o número de camisetas: '))# recebe a entrada e verifica se e um valor valido
            if num > 20000:
                print('Número de camisetas acima do permitido. Tente novamente.')
            else:
                if num < 20:
                    return num, 0
                elif num < 200:
                    return num, 0.05
                elif num < 2000:
                    return num, 0.07
                elif num <= 20000:
                    return num, 0.12
        except ValueError:
            print('Entrada inválida. Digite um número.')

def frete(): #funcao para escolha do frete 
    while True:
        print('\nEscolha o tipo de frete:')
        print('1 - Transportadora - R$ 100.00')
        print('2 - Sedex - R$ 200.00')
        print('0 - Retirar na fábrica - R$ 0.00)')
        opcao_frete = input('Digite a opção de frete: ') # recebe a entrada e verifica se e um valor valido
        if opcao_frete == '1':
            return 'Transportadora', 100
        elif opcao_frete == '2':
            return 'Sedex', 200
        elif opcao_frete == '0':
            return 'Retirar na fábrica', 0
        else:
            print('Opção de frete inválida. Tente novamente.')


nome_modelo, valor_unitario = escolha_modelo() #solicita o modelo desejado e seu valor unitario
num, desconto = num_camisetas() #solicita o numero de camisetas e aplica desconto
quantidade_com_desconto = num * (1 - desconto) #calcula a quantidade com desconto
nome_frete, valor_frete = frete() #solicita a opcao de frete e seu valor
valor_total = (valor_unitario * quantidade_com_desconto) + valor_frete #calcula o valor total

#imprime o valor total
print(f'\nTotal: R$ {valor_total:.2f} (Modelo: {valor_unitario:.2f} * Quantidade (com desconto): {quantidade_com_desconto} + frete: {valor_frete:.2f})')


