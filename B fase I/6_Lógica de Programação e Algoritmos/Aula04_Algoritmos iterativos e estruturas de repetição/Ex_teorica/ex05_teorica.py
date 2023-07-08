'''
Exercício 05: Escreva um algoritmo que realiza um login em um sistema. o usuário deve informar seu nome e senha.
'''

while True:
    nome = input('Qual o seu nome?')
    if(nome != 'Carlos'):
        continue
    senha = input('Qual sua senha?')
    if(senha == 'uninter'):
        break
print('Acesso concedido.')