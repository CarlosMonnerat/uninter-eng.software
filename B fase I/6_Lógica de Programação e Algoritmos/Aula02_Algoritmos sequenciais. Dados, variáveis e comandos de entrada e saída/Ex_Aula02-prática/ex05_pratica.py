'''
Exercício 05: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60,00 por dia e R$0,15 por km rodado.
'''

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preco = 60 * dias + 0.15 * km

print('Foram percorridos: %.2f Km' %km)
print('Dias alugado: %i dias' %dias )
print('Valor do aluguel: R$%.2f' %preco)