casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos', end='')
print(f' a prestação será de R$:{prestacao:.2f}')

porcentagem = 30/100 * salario
if (prestacao > porcentagem):
    print('Seu empréstimo foi negado')

else:
    print('Seu empréstimo foi aceito')
