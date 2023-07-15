# -------------------- ENTRADA DE VARIÁVEIS ----------------------------------
print('Bem-vindo a Loja do Carlos Henrique Monnerat Quintanilha')
valor = float(input('Entre com o valor do produto: '))
qtd = int(input('Entre com a quantidade do produto: '))

# --------------------- VALIDAÇÃO E CALCULO DO DESCONTO ----------------------------
if(qtd < 200):                          # Caso a quantidade de produto seja menor que 200, o programa executará estas instruções
    desconto = 0                        #0% de desconto

elif(qtd < 1000):                       #Caso seja maior ou igual a 200, porém menor que 1000, o programa executará estas instruções
    desconto = valor * qtd * (5 / 100)  #5% de desconto

elif(qtd < 2000):                       #Caso seja maior ou igual a 1000, porém menor que 2000, o programa executará estas instruções
    desconto = valor * qtd * (10 / 100) #10% de desconto

else:                                   #Caso seja maior ou igual a 2000, o programa executará estas instruções
    desconto = valor * qtd * (15 / 100) #15% de desconto

# ------------------------ CALCULO DOS PREÇOS ------------------------------------------
preco_sem = valor * qtd
preco_com = preco_sem - desconto

# ----------------------- SAIDA COM OS RESULTADOS -----------------------------------
print('O valor SEM desconto: R$ {:.2f}' .format(preco_sem))
print('O valor COM desconto: R$ {:.2f}' .format(preco_com))


