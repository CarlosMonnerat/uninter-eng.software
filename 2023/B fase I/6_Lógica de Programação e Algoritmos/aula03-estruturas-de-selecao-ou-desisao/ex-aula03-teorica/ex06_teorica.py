'''
Exercício 06: Escreva um algoritmo que lê um nome e uma idade.
* Caso o nome digitado seja Vinicius, escreva isso na tela.
* Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor.
Se for maior que 100 anos, informe que esta pessoa possivelmente não existe.
'''

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if(nome == 'Vinicius'):
    print(nome)
else:
    if(idade < 18):
        print('Menor de idade!')
    elif(idade > 100):
        print('Provavelmente não existe.')