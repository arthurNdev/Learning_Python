nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média foi {media}')
    print('Você está aprovado!')

elif media < 5:
    print(f'Sua média foi {media}')
    print('Você está de recuperação!')

elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media}')
    print('Você está de recuperação!')
