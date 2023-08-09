from random import randint
print('-' * 30)
print(f'JOGA NA MEGA SENA')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, jogos):
    lista = [[randint(0, 50)], [randint(0, 50)], [randint(0, 50)],
             [randint(0, 50)], [randint(0, 50)], [randint(0, 50)]]
    lista.sort()
    print(f'Jogo {c + 1}: {lista}')
