from random import randint
from time import sleep
items = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))

#Escrevendo JOKENPO com um atraso de 1 segundo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 15)
print(f'O computador jogou {items[computador]}')
print(f'Você jogou {items[jogador]}')
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!!!')
