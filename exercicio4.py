# mensagem de boas vindas
print('\nBem vindos a empresa do João Márcio Calazans Britto')

#lista de funcionários e variável id_global
lista_funcionarios = []
id_global = 4870260  # inicializando com o valor inicial do meu ru


def cadastrar_funcionario(id): # funcao cadastrar_funcionario
    print(f'\nId do Funcionário: {id}')
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))
    
    funcionario = { # cria dicionario com os dados do funcionario
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    lista_funcionarios.append(funcionario.copy()) # adicionando o dicionario a lista de funcionarios
    print(f'Funcionário {nome} cadastrado com sucesso!')


def consultar_funcionarios(): #função consultar_funcionarios
    while True:
        print('\n---------- Menu de Consulta ----------')
        print('\n1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Setor')
        print('4. Retornar ao menu')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            # consultar todos
            if lista_funcionarios:
                print('\nTodos os funcionários:')
                for funcionario in lista_funcionarios:
                    print(f"id: {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salario: {funcionario['salario']}\n")
            else:
                print('\nNão há funcionários cadastrados.')
        
        elif opcao == '2':
            # consulta por id
            id_consulta = int(input('Digite o ID do funcionário: '))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print('\nFuncionário encontrado:')
                    print(f"id: {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salario: {funcionario['salario']}\n")
                    encontrado = True
                    break
            if not encontrado:
                print(f'Funcionário com ID {id_consulta} não encontrado.')
        
        elif opcao == '3':
            # consulta por setor
            setor_consulta = input('Digite o setor a ser consultado: ')
            encontrados = [funcionario for funcionario in lista_funcionarios if funcionario['setor'] == setor_consulta]
            if encontrados:
                print(f'\nFuncionários no setor {setor_consulta}:')
                for funcionario in encontrados:
                    print(f"id: {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salario: {funcionario['salario']}\n")
            else:
                print(f'Nenhum funcionário encontrado no setor {setor_consulta}.')
        
        elif opcao == '4':
            # retornar ao menu principal
            return
        
        else:
            print('Opção inválida. Tente novamente.')


def remover_funcionario(): # função remover_funcionario
    id_remover = int(input('Digite o ID do funcionário a ser removido: '))
    encontrado = False
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remover:
            lista_funcionarios.remove(funcionario)
            print(f'Funcionário com ID {id_remover} removido com sucesso.')
            encontrado = True
            break
    if not encontrado:
        print(f'Funcionário com ID {id_remover} não encontrado.')

# menu principal
while True:
    print('\n---------- Menu Principal -----------')
    print('1. Cadastrar Funcionário')
    print('2. Consultar Funcionário')
    print('3. Remover Funcionário')
    print('4. Encerrar Programa')
    
    opcao_principal = input('Escolha uma opção: ')
    
    if opcao_principal == '1':
        id_global += 1
        cadastrar_funcionario(id_global)
        
    elif opcao_principal == '2':
        consultar_funcionarios()
        
    elif opcao_principal == '3':
        remover_funcionario()
        
    elif opcao_principal == '4':
        print('Encerrando o programa...')
        break
    
    else:
        print('Opção inválida. Tente novamente.')

