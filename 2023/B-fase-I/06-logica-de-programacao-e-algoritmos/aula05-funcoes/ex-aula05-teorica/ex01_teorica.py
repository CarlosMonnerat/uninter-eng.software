'''
Exercício 01: Escreve uam rotina que crie umma borda ao redor de uma palavra para destacá-la como sendo um título. A
rotina deve receber como paâmetro a palavra a ser destacada. O tamanho da caixa de texto deverá ser adaptável de acordo
com o tamanho da palavra.
'''

# Função
def borda(s1):
    tam = len(s1)
    if tam:                         # Só imprime caso exista algum caractere
        print('+','-' * tam,'+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

# Programa Princial
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')
borda('Exercício de Python')