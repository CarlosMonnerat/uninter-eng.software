'''
Exerxício 01: Desenvolva um algoritmo que solicite ao usuário dois números inteiros.
Imprima a soma destes dois números na tela.
'''

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))

# Forma clássica
res = 'O resultado da soma de %.i com %.i é %.i' %(n1, n2, n1+n2)
print(res)

# Forma moderna
res2 = 'o resultado da soma de {} com {} é {}' .format(n1, n2, n1+n2)
print(res2)
