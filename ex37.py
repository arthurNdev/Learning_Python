from random import randint
cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    valor = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? [P/I}: ').upper()
    computador = randint(0, 10)
    if (valor + computador) % 2 == 0 and escolha == 'P':
        print('-' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} PAR')
        print('-' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif (valor + computador) % 2 != 0 and escolha == 'I':
        print('-' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} ÍMPAR')
        print('-' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif (valor + computador) % 2 == 0 and escolha == 'I':
        print('-' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} PAR')
        print('-' * 30)
        print('Você PERDEU!')
        print('=-' * 20)
        break
    elif (valor + computador) % 2 != 0 and escolha == 'P':
        print('-' * 30)
        print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} ÍMPAR')
        print('-' * 30)
        print('Você PERDEU!')
        print('=-' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes')
