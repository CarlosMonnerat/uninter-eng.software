'''
                    Desacoplamento de parâmetros em funções:
exercício 01: escreva um algoritmo que faça o somatório de diversos valores, porém, sem saber quantos valores serão
somados. Pode ser que sejam somente 2, ou então 10, ou mesmo 100 números
'''

def soma(*num):             # '*' = Desempacotamento: Transforma a variável 'num' em uma Tupla
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

# Programa Principal
print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))

