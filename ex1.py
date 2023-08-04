n1 = float(input('Qual a sua primeira nota?: '))
n2 = float(input('Qual a sua segunda nota?: '))
media = (n1 + n2) / 2
if (media >= 6):
    print(f'Sua média foi {media}, parabéns!')
elif (media < 6):
    print(f'Sua média foi {media}, estude mais!')