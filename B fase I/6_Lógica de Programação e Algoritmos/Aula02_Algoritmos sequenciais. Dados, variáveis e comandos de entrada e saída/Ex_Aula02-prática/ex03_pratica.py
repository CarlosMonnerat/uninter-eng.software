'''
Exercício 03: Execute as seguintes atribuições:
s1 = 'ant', s2 = 'bat', s3 = 'cod'.
Agora, utilizando operadores + e *, crie as saídas a seguir:
a) 'ant bat cod'
b) 'ant ant ant ant ant ant ant ant ant ant'
c) 'ant bat bat cod cod cod'
d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
'''

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

#a)
a = s1+' '+s2+' '+ s3

#b)
b = (s1+' ')*10

#c)
c = s1+' '+(s2+' ')*2+' '+(s3+' ')*3

#d)
d = (s1+' '+s2+' ')*7

#e)
e = ((s2+' ')*2 + s3+' ')*5

#prints
print(a)
print(b)
print(c)
print(d)
print(e)