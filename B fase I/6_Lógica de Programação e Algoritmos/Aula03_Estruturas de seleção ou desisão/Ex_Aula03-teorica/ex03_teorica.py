'''
Exercício 03: Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando.
Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um
algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não.
'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

if(n1 >= 7 and n2 >= 7 and n3 >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')