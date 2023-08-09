from random import randint
print('Irei pensar em um número e você terá que advinhar')
print('O número que eu pensei está entre 0 e 10.')
maquina = randint(0, 10)
cont = 1
pessoa = int(input('Qual o seu palpite? '))
while pessoa != maquina:
    if maquina > pessoa:
        pessoa = int(input('Mais... Tente novamente: '))
        cont += 1
    elif maquina < pessoa:
        pessoa = int(input('Menos... Tente novamente: '))
        cont += 1
print(f'Parabéns você acertou com {cont} tentativas, o número que eu pensei foi o {maquina}')
