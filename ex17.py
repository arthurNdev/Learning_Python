lado1 = float(input('Qual o tamanho do primeiro lado? '))
lado2 = float(input('Qual o tamanho do segundo lado? '))
lado3 = float(input('Qual o tamanho do terceiro lado? '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('PODE formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')

    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('ESCALENO!')

    else:
        print('ISÓSCELES!')

else:
    print('NÃO PODE formar um triângulo!')
