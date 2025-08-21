'''
Exercício 02: Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele
deseja realizar: adição(+), subtração(-), multiplicação(*), divisão(/) e sair. Exiba na tela o resultado da
operação desejada.
    Repita até que a opção saída seja escolhida.
'''
print('CALCULADORA:')
print('adição(+)')
print('subtração(-)')
print('multiplicação(*)')
print('divisão(/)')
print('Digite "sair" para encerrar!')
print('----------------------------------')

op = input('Qual operação deseja realizar? ')
while op != 'sair':
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
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

    op = input('Qual operação deseja realizar? ')

print("Ok, encerrando o programa...")
