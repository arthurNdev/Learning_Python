lista = []
pos = 1
for c in range(1, 6):
    lista.append(input(f'Digite um valor para a posição {pos}: '))
    pos += 1
print('=-' * 20)
print(f'Você digitou os valores ', end='')
for val in lista:
    print(val, end=' ')

print(f'\nO maior valor digitado foi {max(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i + 1}', end=' ')

print(f'\nO menor valor digitado foi {min(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i + 1}', end=' ')
