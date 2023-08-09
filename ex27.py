n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {cont} vezes')
if cont == 2:
    print(f'Portanto o número {n} É PRIMO!')
else:
    print(f'Portanto o número {n} NÃO É PRIMO!')
