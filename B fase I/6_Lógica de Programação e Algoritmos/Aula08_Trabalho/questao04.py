#---------------- VARIÁVEIS GLOBAIS ----------------
lista_colaboradores = []
id_global = 0

#-------------------------------------------------- FUNÇÕES ----------------------------------------------------
    # CADASTRAR
def cadastrar_colaborador(id):
    print('******************************************************************************')
    print('------------------------- CADASTRAR COLABORADOR ------------------------------')
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
                for colaborador in lista_colaboradores:   # Irá percorrer toda a lista de colaboradores
                    print('-------------------------------')
                    for key, value in colaborador.items():
                        print('{}: {}'.format(key, value))
                break
            if op_consultar == '2':
                info = input('Informe o ID do colaborador: ')
                # NAO SEI
                break
            if op_consultar == '3':
                info = input('Informe o setor do(s) colaborador(es): ')
                # NAO SEI
                break
            if op_consultar == '4':
                # Retomar ao Menu
                return

    # REMOVER COLABORADOR
def remover_colaborador():
    print('******************************************************************************')
    print('------------------------- REMOVER COLABORADOR ------------------------------')






#------------------------------------------ PROGRAMA PRINCIPAL -------------------------------------------------

print('Bem-vindo ao Controle de Colaboradores do Carlos Henrique Monnerat Quintanilha')
print('******************************************************************************')
while True:
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
            break
        elif op_principal == '3':
            remover_colaborador()
            break
        elif op_principal == '4':
            print('Encerrando o programa...')
            break
