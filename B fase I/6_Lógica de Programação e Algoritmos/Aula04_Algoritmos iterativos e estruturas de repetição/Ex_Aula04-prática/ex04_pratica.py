'''
Exercício 04: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se a pessoa
tiver menos de 3 anos, o ingresso será gratuito, se tiver entre 3 e 12 anos, custará R$15, se tiver mais de 12 anos
custará R$30.
    * Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.
    * Encerre o laço usando um break quando o usuário digitar sair.
    * Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro arrecadado
e a média de idade das pessoas.
'''
pessoas = 0
arrecadado = 0
soma = 0

idade = input('Qual sua idade? ')
while True:
    if idade == 'sair':
        print('----------------------------------')
        print('Total de pessoas: {}' .format(pessoas))
        print('Total arrecadado: R${}'.format(arrecadado))
        if pessoas != 0:
            media = soma / pessoas
            print('Média de idade: %.2f' %media)
        break
    idade = int(idade)
    if idade < 3:
        preco = 0
        pessoas +=1
        arrecadado += preco
        soma += idade
    elif idade > 12:
        preco = 30
        pessoas += 1
        arrecadado += preco
        soma += idade
    else:
        preco = 15
        pessoas += 1
        arrecadado += preco
        soma += idade
    print(' Preço do ingresso: R${},00'.format(preco))
    idade = input('Qual sua idade? ')
