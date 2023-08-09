from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nascimento
alistamento = 18 - idade
ano_alistamento = nascimento + 18

if idade < 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')
    print(f'Faltam {alistamento} anos para o seu alistamento')
    print(f'Seu alistamento será em {ano_alistamento}')

elif idade > 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')
    print(f'O seu alistamento foi em {ano_alistamento}')

else:
    print(f'Quem nasceu {nascimento} tem {idade} anos em {ano}')
    print(f'O seu alistamento será esse ano')
