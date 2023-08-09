n = s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores vale {s}')
