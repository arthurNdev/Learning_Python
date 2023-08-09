cont_idade_mais18 = 0
cont_f_menos20 = 0
cont_m = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    if idade > 18:
        cont_idade_mais18 += 1
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').upper()
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f_menos20 += 1
    print('-' * 20)
    iniciar = ' '
    while iniciar not in 'SN':
        iniciar = input('Quer continuar? [S/N]').upper()
    if iniciar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont_idade_mais18}')
print(f'Ao todo temos {cont_m} homens cadastrados')
print(f'E temos {cont_f_menos20} mulheres com menos de  20 anos')
