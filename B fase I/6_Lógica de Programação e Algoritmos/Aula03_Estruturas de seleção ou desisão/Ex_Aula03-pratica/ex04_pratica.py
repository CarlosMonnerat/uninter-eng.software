'''
Exercício 04: Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja
realizar: adição(+), subtração(-), multiplicação(*), ou divisão(/). Exiba na tela o resultado da operação desejada.
'''
print('CALCULADORA:')
print('adição(+)')
print('subtração(-)')
print('multiplicação(*)')
print('divisão(/)')
print('----------------------------------')
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input('Qual operação deseja realizar? ')
print('----------------------------------')

if op == '+':
    res = n1 + n2
    print('Resultado: {} + {} = {}' .format(n1, n2, res))
elif op == '-':
    res = n1 - n2
    print('Resultado: {} - {} = {}' .format(n1, n2, res))
elif op == '*':
    res = n1 * n2
    print('Resultado: {} * {} = {}' .format(n1, n2, res))
elif op == '/':
    res = n1 / n2
    print('Resultado: {} / {} = {}' .format(n1, n2, res))
else:
    print("Operação Invalida! Verifique e tente novamente.")
