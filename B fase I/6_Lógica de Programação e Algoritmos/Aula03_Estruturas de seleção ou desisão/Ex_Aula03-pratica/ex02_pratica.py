'''
Exercício 02: Traduza as afirmações a seguir para condicionais em Python:
a) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios"
b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!"
c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultam em True, escreva: "Você escapou!"
d) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não
é um ano bissexto.
e) Se ambas as variáveis booleanas cima e baixo forem True, escreve: "Decida-se!", caso contrário, escreva:
"Você escolheu um caminho!"
'''

#a)
if idade > 60:
    print('Você tem direitos aos benefícios')

#b)
if dano > 10 and escudo == 0:
    print('Você está morto!')

#c)
if (norte or sul or leste or oeste):
    print('Você escapou!')

#d)
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

#e)
if (cima and baixo):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')