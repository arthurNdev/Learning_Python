sexo = input('Informe seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, digite o seu sexo [M/F]: ').upper()
print('Fim do cadastro.')
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.')
else:
    print('Sexo feminino registrado com sucesso.')
