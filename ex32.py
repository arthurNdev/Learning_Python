print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
t1 = 0
t2 = 1
t3 = t1 + t2

termos = int(input('Quantos termos você quer mostrar? '))
print(f'{t1} -> {t2} -> ', end='')
for c in range(0, termos - 2):
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
