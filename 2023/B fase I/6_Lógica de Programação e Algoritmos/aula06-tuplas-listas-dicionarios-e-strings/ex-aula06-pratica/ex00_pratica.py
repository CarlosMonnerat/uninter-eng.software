'''
Exercício de fixação: Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
        notas = [9,7,7,10,3,9,6,6,2]
    a)Encontrar quantos alunos tiraram nota 7
    b)Alterar a última nota para 4
    c)Encontrar a meior nota
    d)Ordenar a lista de notas
    e)A média das notas
'''
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#a)
n = notas.count(7)
print('{} alunos tiraram nota 7 (sete)'.format(n))

#b)
notas[-1] = 4
print(notas)
