'''
Exercício 04: Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas.
Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana.
Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total
a pagar do produto escolhido e mostrá-lo na tela.
Considere que uma maçã custa R$2,30, uma laranja, R$3,60 e uma banana R$1,85
'''

print('Escolha o ítem que deseja:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))

if(produto == 1):
    precof = qtd * 2.3
    print('Você comprou {} maças. Total à pagar: R${}' .format(qtd, precof))
else:
    if(produto == 2):
        precof = qtd * 3.6
        print('Você comprou {} laranjas. Total à pagar: R${}'.format(qtd, precof))
    else:
        if (produto == 3):
            precof = qtd * 1.85
            print('Você comprou {} bananas. Total à pagar: R${}'.format(qtd, precof))
        else:
            print('Produto Inexistente!')