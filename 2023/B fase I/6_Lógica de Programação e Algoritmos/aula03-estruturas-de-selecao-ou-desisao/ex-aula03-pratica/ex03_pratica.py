'''
Exercício 03: Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
Verifique se os valores formam um triângulo e classifique como:
a)Equilátero (Três lados iguais)
b) Isósceles (Dois lados iguais)
c) Escaleno (Três lados diferentes)
Lembre-se de que, para formar um triângulo, nenhum dos lados poder ser igual a zero, e um lado não pode ser maior do
que a soma dos outros dois
'''

print("Digite os lados do triângulo.")
l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 == 0 or l2 == 0 or l3 == 0) or (l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2):
    print('Não é um Triângulo!')
elif (l1 == l2 and l2 == l3):
    print('Triângulo: Equilátero')
elif (l1 == l2 or l1 == l3 or l2 == l3):
    print('Triângulo: Isósceles')
else:
    print('Triângulo: Escaleno')