lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        continue
    else:
        print('ERRO. Opção não é válida!')
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado dentro da lista')
