n = int(input('Digite um número para ver a sua tabuada: '))
cont = 1
for c in range(0, 10):
    tabuada = n * cont
    print(f'{n} x {cont} = {tabuada}')
    cont += 1
