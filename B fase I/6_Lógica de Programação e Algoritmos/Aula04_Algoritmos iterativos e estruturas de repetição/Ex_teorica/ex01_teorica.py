'''
Exercício 01: Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pela
usuário e que sejam número pares.
'''

inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))

x = inicial
while(x <= final):
    if (x % 2 == 0):
        print(x)
    x+=1
