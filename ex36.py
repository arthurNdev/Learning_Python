while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 25)
    cont = 1
    if valor < 0:
        break
    for c in range(0, 10):
        print(f'{valor} x {cont} = {valor * cont}')
        cont += 1
print('PROGRAMA ENCERRADO!')
