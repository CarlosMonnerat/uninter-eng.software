'''
Exercício 02: Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sistema. Cada
produto comprado deverá ser registrado com seu nome, quantidade e valor unitário.
'''

#       Solução 1:
item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])  # '[:]' = indica que é uma copia, mas não é a mesma lista.
    item.clear()

print(mercado)

'''
#       Solução 2 (Simplificada):
mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])

print(mercado)
'''

