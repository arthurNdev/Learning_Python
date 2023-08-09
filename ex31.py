from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = 0
somar = n1 + n2
multiplicar = n1 * n2
subtrair = n1 - n2
dividir = n1 / n2

while escolha != 7:
    print('[1] somar\n[2] multiplicar\n[3] subtrair\n[4] dividir\n[5] maior\n[6] novos números\n[7] sair')
    escolha = int(input('>>>>> Qual a sua opção? '))
    if escolha == 1:
        print(f'O resultado de {n1} + {n2} é {somar}')
        print('=-' * 13)

    elif escolha == 2:
        print(f'O resultado de {n1} x {n2} é {multiplicar}')
        print('=-' * 13)

    elif escolha == 3:
        print(f'O resultado de {n1} - {n2} é {subtrair}')
        print('=-' * 13)

    elif escolha == 4:
        print(f'O resultado de {n1} ÷ {n2} é {dividir}')
        print('=-' * 13)

    elif escolha == 5:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que o número {n1}')
        else:
            print(f'{n1} e {n2} são iguais')
        print('=-' * 13)

    elif escolha == 6:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-' * 13)

    elif escolha == 7:
        print('Programa finalizado')

    else:
        print('Opção inválida. Tente novamente')
sleep(10)
