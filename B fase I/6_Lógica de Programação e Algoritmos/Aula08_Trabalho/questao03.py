    # Apresentação
print('Bem-vindo ao PetShop do Carlos Henrique Monnerat Quintanilha')

# Funções
def cachorro_peso(pergunta):
    while True:
        try:
            peso = int(input(pergunta))
            if(peso > 0 and peso < 3):
                base = 40
                break
            elif(peso >= 3 and peso < 10):
                base = 50
                break
            elif(peso >= 10 and peso < 30):
                base = 60
                break
            elif(peso >= 30 and peso < 50):
                base = 70
                break
            elif(peso <= 0):
                print('-------------------------------------------------------------------')
                print('Peso inválido.\nPor favor tente novamente')
                continue
            elif (peso >= 50):
                print('-------------------------------------------------------------------')
                print('Não aceitamos cachorros tão grandes.\nPor favor entre com o peso do cachorro novamente')
                continue
        except:
            print('-------------------------------------------------------------------')
            print('Você digitou um valor não numérico.\nPor favor entre com o peso do cachorro novamente')
            continue
    return base

def cachorro_pelo(pergunta):
    while True:
        print('Entre com o PELO do cachorro: ')
        print('c - Pelo Curto')
        print('m - Pelo Médio')
        print('l - Pelo Longo')
        pelo = input(pergunta)
        if(pelo != 'c' and pelo != 'm' and pelo != 'l'):
            print('----------------------------------')
            print('Pelo inválido. Tente novamente.')
            continue
        elif(pelo == 'c'):
            multiplicador = 1
            break
        elif (pelo == 'm'):
            multiplicador = 1.5
            break
        elif (pelo == 'l'):
            multiplicador = 2
            break
    return multiplicador

def cachorro_extra(pergunta):
    extra = 0
    while True:
        print('Deseja adicionar mais algum serviço?')
        print('1 - Corte de Unhas - R$10,00')
        print('2 - Escovar Dentes - R$12,00')
        print('3 - Limpeza de Orelhas - R$15,00')
        print('0 - Não desejo mais nada')
        add = input(pergunta)
        if(add != '1' and add != '2' and add != '3' and add != '0'):
            print('-------------------------------------')
            print('Adicional inválido. Por favor tente novamente.')
            continue
        elif(add == '1'):
            extra += 10
            continue
        elif (add == '2'):
            extra += 12
            continue
        elif (add == '3'):
            extra += 15
            continue
        elif (add == '0'):
            extra += 0
            break
    return extra



# Programa Principal
base = cachorro_peso('Entre com o PESO do cachorro: ')
multiplicador = cachorro_pelo('>> ')
extra = cachorro_extra('>> ')

total = base * multiplicador + extra

print('-------------------------------------')
print('Total a pagar: R${:.2f}'.format(total))
