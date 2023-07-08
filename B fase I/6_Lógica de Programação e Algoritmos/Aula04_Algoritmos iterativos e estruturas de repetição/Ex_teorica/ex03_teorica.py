'''
Exercício 03: Crie um algoritmo que receba um valor do tipo inteiro via teclado. No entanto,
o programa só deve aceitar, obrigatóriamente valores inteiros e positivos.
Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado.
'''

x = int(input('Dgite um valor maior que zero: '))
while(x <= 0):
    x = int(input('Dgite um valor maior que zero: '))
print('Você digitou {}. Encerrando o programa...' . format(x))