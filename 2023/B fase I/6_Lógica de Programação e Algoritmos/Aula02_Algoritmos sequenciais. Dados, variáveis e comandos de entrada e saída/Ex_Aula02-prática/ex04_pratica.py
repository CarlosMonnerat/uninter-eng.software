'''
Exercício 04: Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto
a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.
'''

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0-100)%: '))

desconto = (preco * p)/100
preco_final = preco - desconto

print('Seu desconto é de R$%.2f' %desconto)
print('O preço final será de R$%.2f' %preco_final)