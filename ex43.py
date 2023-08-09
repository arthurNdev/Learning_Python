numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3) + 1} posição')
num_par = False
for num in numero:
    if num % 2 == 0:
        num_par = True
if num_par is True:
    print(f'Os valores pares digitados foram ', end='')
    for num in numero:
        if num % 2 == 0:
            print(num, end=' ')
if not num_par:
    print('Nenhum número par foi digitado')
