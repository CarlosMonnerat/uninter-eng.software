'''
Exercício 05: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
Calcule o preço de acordo com a tabela: (Apostila)
'''

kwh = float(input('Quantos kWh? '))
tipo = input('Qual o tipo de instalação? (R, C ou I) ')

if(tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif(tipo == 'C'):
    if kwh <= 1000:
        preco = 0.6
    else:
        preco = 0.65
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação inválida!')

print('Total a pagar: R${}' .format(kwh * preco))
