'''
Exercício 03: Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar
esse mesmo valor. Para simplificar, vamos com cédulas de R$100, R$50. R$20, R$10, R$5 e R$1
'''

valor = int(input('Digite um valor: ')) #R$522

while True:
    if valor >= 100:
        cedula100 = valor // 100
        valor -= cedula100 * 100
        print('Cédulas de 100: {}'.format(cedula100))
        if not valor:
            break
    if valor >= 50:
        cedula50 = valor // 50
        valor -= cedula50 * 50
        print('Cédulas de 50: {}'.format(cedula50))
        if not valor:
            break
    if valor >= 20:
        cedula20 = valor // 20
        valor -= cedula20 * 20
        print('Cédulas de 20: {}'.format(cedula20))
        if not valor:
            break
    if valor >= 10:
        cedula10 = valor // 10
        valor -= cedula10 * 10
        print('Cédulas de 10: {}'.format(cedula10))
        if not valor:
            break
    if valor >= 5:
        cedula5 = valor // 5
        valor -= cedula5 * 5
        print('Cédulas de 5: {}'.format(cedula5))
        if not valor:
            break
    if valor:       #Verifica se sobrou alguma coisa
        cedula1 = valor
        print('Cédulas de 1: {}'.format(cedula1))
        break