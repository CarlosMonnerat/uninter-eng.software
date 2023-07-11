    #Apresentação e Cardápio
print('Bem-vindo a Sorveteria do Carlos Henrique Monnerat Quintanilha')
print('--------------------------------------Cardápio--------------------------------------')
print('| Nº DE BOLAS  | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1       |         R$ 6,00        |      R$ 7,00       |       R$ 8,00       |')
print('|      2       |         R$ 11,00       |      R$ 13,00      |       R$ 15,00      |')
print('|      3       |         R$ 15,00       |      R$ 18,00      |       R$ 21,00      |')
print('------------------------------------------------------------------------------------')

valor = 0     # Acumulador para apresentar o valor total no final do programa

    #Looping e Validação das entradas:
while True:                                            # Cria um loop de execução das instruções.
    sabor = input('Entre com o sabor desejado (tr/es/pr): ')
# Verifica se o sabor digitado é válido ou não:
    if(sabor == 'tr'):                                 #Caso o usuário digitar "tr" o código executará estas instruções:
        bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
    # Verifica se o número de bolas de sorvete digitado é válido ou não:
        if(bolas == '1'):
            valor += 6            #Soma o preço do sorvete ao acumulador de acordo com o sabor e nº de bolas escolhidos.
            print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00')
        elif(bolas == '2'):
            valor += 11
            print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$ 11,00')
        elif(bolas == '3'):
            valor += 15
            print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$ 15,00')
        else:  #Caso o nº de bolas de sorvete for inválido, irá printar a msg a baixo, e o programa voltará para o início do looping.
            print('Número de bolas de sorvete inválido. Tente novamente')
            continue

    elif(sabor == 'pr'):   #Caso o usuário digitar "pr" o código executará estas instruções e o processo seguirá de forma análoga:
        bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
        if (bolas == '1'):
            valor += 7
            print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$ 7,00')
        elif (bolas == '2'):
            valor += 13
            print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$ 13,00')
        elif (bolas == '3'):
            valor += 18
            print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$ 18,00')
        else:
            print('Número de bolas de sorvete inválido. Tente novamente')
            continue

    elif (sabor == 'es'):       #Caso o usuário digitar "es" o código executará estas instruções e o processo seguirá de forma análoga:
        bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
        if (bolas == '1'):
            valor += 8
            print('Você pediu 1 bola de sorvete no sabor ESPECIALL: R$ 8,00')
        elif (bolas == '2'):
            valor += 15
            print('Você pediu 2 bolas de sorvete no sabor ESPECIALL: R$ 15,00')
        elif (bolas == '3'):
            valor += 21
            print('Você pediu 3 bolas de sorvete no sabor ESPECIALL: R$ 21,00')
        else:
            print('Número de bolas de sorvete inválido. Tente novamente')
            continue
    else:
        print('Sabor inválido. Tente novamente')
        continue
# Verifica se o usuário deseja comprar mais alguma coisa:
    add = input('Deseja mais algum sorvete (s/ digite outra tecla)?:  ')
    if (add == 's'):  #Caso positivo, o programa retorna para o inicio do looping
        continue
    else:                   #Caso negativo, o programa imprime na tela o valor total a ser pego e encerra o programa.
        print('-----------------------------------------------')
        print('Valor total a ser pago: R${:.2f}'.format(valor))
    break