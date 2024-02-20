'''
Exercício 03: Suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar
esses jogos informando o nome e a qual videogame ele pertence.
*   Para isso, crie um menu de opções contendo: Cadastrar novo item, listar tudo que foi cadastrado e sair.
*   Para resolver esse exercício, crie pelo menos uma função para cada item do menu
*   Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados.
'''

    # Funções
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')         #   'r' = Read,     't' = .txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')          #  'w' = Write,   't' = .txt,     '+' = Caso o arquivo não exista, crie!
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} criado com sucesso.'.format(nomeArquivo))

def cadastrarJogo(nomeAquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeAquivo, 'at')           # 'a' = Write, mas preserva o conteúdo se já existir
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{}; {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')         # 'r' = Read
    except:
        print('Erro ao ler o arquivo')
    else:
        print('-------Lista dos Jogos --------')
        print(a.read())
        print('-------------------------------')
    finally:
        a.close()


    # Programa Principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente!')
    criaArquivo(arquivo)

while True:
    print('-----------------MENU--------------------')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastro')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção Cadastrar novo game selecionada: \n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção Listar selecionada: \n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break