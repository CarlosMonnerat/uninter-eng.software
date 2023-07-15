#---------------------------------VARIÁVEIS GLOBAIS ------------------------------------
lista_colaboradores = []
id_global = 0

#------------------------------------- FUNÇÕES ------------------------------------------
    # CADASTRAR COLABORADOR
def cadastrar_colaborador(id):
    print('******************************************************************************')
    print('------------------------- CADASTRAR COLABORADOR ------------------------------')
    print('id do colaborador: {}'.format(id))
    nome = input('Por favor entre com o nome: ')
    setor = input('Por favor entre com o setor: ')
    pagamento = float(input('Por favor entre com o pagamento(R$): '))
    dicionario = {'id': id, 'nome': nome, 'setor': setor, 'pagamento': pagamento}

    lista_colaboradores.append(dicionario)

    # CONSULTAR COLABORADOR
def consultar_colaboradores():
    print('******************************************************************************')
    print('------------------------- CONSULTAR COLABORADOR ------------------------------')
    while True:
        print('Escolha a opção desejada:')
        print('1 - Consultar TODOS')
        print('2 - Consultar Colaborador por ID')
        print('3 - Consultar Colaborador por Setor')
        print('4 - Retornar ao Menu')
        op_consultar = input('>>')

        if op_consultar not in '1234':
            print('opção inválida. Tente novamente')
            print('-------------------------------')
            continue
        else:
            if op_consultar == '1':
                for colaborador in lista_colaboradores:         # Irá percorrer toda a lista de colaboradores
                    print('-------------------------------')
                    for key, value in colaborador.items():      # Percorre por todas chaves e valores do dicionário dentro da lista
                        print('{}: {}'.format(key, value))
                    print('-------------------------------')
            elif op_consultar == '2':
                consulta_id = int(input('Informe o ID do colaborador: '))
                for colaborador in lista_colaboradores:
                    if colaborador['id'] == consulta_id:        # Verifica se o ID digitado pelo usuáro é igual ao da chave do dicionário
                        print('-------------------------------')
                        for key, value in colaborador.items():
                            print('{}: {}'.format(key, value))
                        print('-------------------------------')
            elif op_consultar == '3':
                consulta_setor = input('Informe o setor do(s) colaborador(es): ')
                for colaborador in lista_colaboradores:
                    if colaborador['setor'] == consulta_setor:
                        print('-------------------------------')
                        for key, value in colaborador.items():
                            print('{}: {}'.format(key, value))
                        print('-------------------------------')
            else:
                return      # Retorna para o Menu Principal

    # REMOVER COLABORADOR
def remover_colaborador():
    print('******************************************************************************')
    print('------------------------- REMOVER COLABORADOR ------------------------------')
    remover_id = int(input('Informe o ID do colaborador a ser removido: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == remover_id:
            lista_colaboradores.remove(colaborador)
            print('Colaborador removido com sucesso.')


#------------------------------------ PROGRAMA PRINCIPAL ---------------------------------

print('Bem-vindo ao Controle de Colaboradores do Carlos Henrique Monnerat Quintanilha')
while True:
    print('******************************************************************************')
    print('---------------------------- MENU PRINCIPAL ----------------------------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Colaborador')
    print('2 - Consultar Colaborador(es)')
    print('3 - Remover Colaborador')
    print('4 - Sair')
    op_principal = input('>> ')

    if op_principal not in '1234':
        print('opção inválida. Tente novamente')
        print('-------------------------------')
        continue
    else:
        if op_principal == '1':
            id_global += 1
            cadastrar_colaborador(id_global)
            continue
        elif op_principal == '2':
            consultar_colaboradores()
        elif op_principal == '3':
            remover_colaborador()
        elif op_principal == '4':
            print('Encerrando o programa...')
            break
