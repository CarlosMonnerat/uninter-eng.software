#Função de Saída
print('Olá, mundo!')
print(2+5)
print('2'+'5')
print('O resultado da soma de 2 + 3 é:', 2+3)

#Variaveis
nota = 8.5
dis ='Lógica de programação e algoritmos'
a = 1
b = 5
res = a != b

print('Disciplina:', dis)
print('Nota:', nota)
print(res)

#Strings
frase = 'Olá, mundo!'
s1 = 'A' + '-'*10 + 'B'
s2 = 'Você tirou %.2f na disciplina %s' %(nota, dis)
s3 = 'Você tirou {} na disciplina {}' .format(nota, dis)
tamanho = len(s2)                       #Informa o tamanho da string

print(frase[2])                         #Acesso à apenas uma letra da string
print(s1)
print(s2)
print(s3)
print(s2[0:6])                          #Fatiar uma string
print(tamanho)

#Função de Entrada
idade = input('Qual sua idade?')
print(idade)                            #Recebe uma string

nome = input('Qual o seu nome?')
print('Olá {}, seja bem-vindo!'.format(nome))

nota2 = float(input('Qual nota vc tirou na disciplina?'))   #Converte string para float
print('você tirou {}' .format(nota2))


