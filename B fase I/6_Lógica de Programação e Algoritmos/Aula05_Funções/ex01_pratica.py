'''
Exercício 01: Crie uma Docstring dentro de uma função
'''

def soma(x=0, y=0, z=0):
    """
        Docsting:
    Retorna o somatório de até 3 valores numéricos quaisquer.
    Todos os parâmetros são opcionais.

    x: Valor numérico (opcional)
    y: Valor numérico (opcional)
    z: Valor numérico (opcional)
    """
    return x+y+z

print(soma(3,2))
help(soma)