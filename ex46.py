lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        continue
    else:
        print('Ocorreu um erro')
lista.sort()
print(f'Você digitou os valores {lista}')
