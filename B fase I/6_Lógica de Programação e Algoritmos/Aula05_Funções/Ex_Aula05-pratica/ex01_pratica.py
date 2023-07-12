'''
Exercício 01: Crie uma Docstring dentro de uma função
'''

def soma(x=0, y=0, z=0):
    """---------Docstring-----------
    Função que retorna o somatório de até 3 valores numéricos quaisquer.
    Todos os parâmetros são opcionais.

    :param x: Valor numérico (opcional)
    :param y: Valor numérico (opcional)
    :param z: Valor numérico (opcional)
    :Return: Soma
    """
    return x+y+z

print(soma(3,2))
help(soma)