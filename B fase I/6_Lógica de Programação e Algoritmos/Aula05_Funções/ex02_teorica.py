'''
Exercício 02: Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo
e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, e falso,
caso contrário
'''

# Função
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

# Programa Principal
x = valida_string('Digite uma sting: ', 10, 30)
print('Você digitou a string {}. \n Dado válido. Encerrando o programa...'.format(x))