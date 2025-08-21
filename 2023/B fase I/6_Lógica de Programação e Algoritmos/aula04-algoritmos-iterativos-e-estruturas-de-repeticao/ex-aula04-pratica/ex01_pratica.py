'''
Exercícios 01: Realiza a seguência de print com for e while:
a) Inteiros e 3 até 12, com 12 incluso
b) Inteiros de 0 até 9, exluindo o 9, com passo de 2
'''

#a)
    #While
print('COM WHILE:')
x = 3
while(x <= 12):
    print(x)
    x += 1
print('COM FOR:')
    #for
for i in range(3,13):
    print(i)

#b)
    #While
print('COM WHILE:')
y = 0
while y < 9:
    print(y)
    y += 2
    #for
print('COM FOR:')
for i in range(0,9,2):
    print(i)