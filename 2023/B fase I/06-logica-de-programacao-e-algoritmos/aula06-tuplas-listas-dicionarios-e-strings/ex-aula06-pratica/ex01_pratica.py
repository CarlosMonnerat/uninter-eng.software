'''
Exerício 01: Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada
palavra. Faça um print na tela com o nome da palavra e suas respectivas vogais.
'''

palavras = ('Goku', 'Vegeta', 'Gohan', 'Bulma', 'Piccolo', 'Nº17', 'Nº18', 'Kulilin', 'Majin boo', 'Yancha')

for personagem in palavras:
    print('\nPersonagem: {}. Vogais: '.format(personagem.upper()), end='')
    for letra in personagem:
        if letra.lower() in 'aeiou':            # Se letra está entre 'aeiou'
            print(letra.upper(), end=' ')
