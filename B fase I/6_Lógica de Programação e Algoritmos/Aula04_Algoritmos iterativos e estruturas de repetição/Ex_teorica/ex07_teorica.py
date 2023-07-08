'''
Exercício 07: Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 100, e, para
cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 100.
'''

for tabuada in range(1,11,1):
    print('TABUADA DO {}:'.format(tabuada))
    for i in range(1,11,1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))