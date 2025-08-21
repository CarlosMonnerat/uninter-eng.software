'''
Exercício 03: Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
    Armazene os dados em um dicionário com listas
    Ao encerrar o cadastro, apresente:
        O total de cadastros efetuados
        A média das idades das pessoas
        Uma lista de mulheres com menos de 30 anos
        Uma lista de homens com idade acima da média
'''

cadastro = {'nome':[], 'ano':[], 'sexo':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [s/n] ')
    if terminar.lower() in 'n':
        break
    if terminar.lower() not in 's':
        print('Digite "s" para SIM e "n" para NAO')
        continue

    nome = input('Qual seu nome? ')
    sexo = input('Qual seu sexo? ')
    ano = int(input('Qual seu ano de nascimento? '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)