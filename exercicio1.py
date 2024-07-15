#imprime a apresentacao na tela e pede informacoes do pedido ao usuario
print('Bem vindo(a) a loja do João Márcio Calazans Britto\n')
valorDoPedido = float(input('Digite o valor do pedido: R$ '))
quantidadeDeParcelas = int(input('Digite a quantidade de parcelas: '))

#condicional para o calculo de juros
if quantidadeDeParcelas < 4:
    juros = 0
elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
    juros = 4/100
elif quantidadeDeParcelas >=6 and quantidadeDeParcelas <9:
    juros = 8/100
elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
    juros = 16/100
else:
    juros = 32/100

#calcula e imprime na tela o valor das parcelas e o total do pedido 
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeDeParcelas
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas

print(f'\nO valor das parcelas é de: R$ {valorDaParcela:.2f}\nO valor total parcelado é de: R$ {valorTotalParcelado:.2f}\n')