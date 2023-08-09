valor = prod_mais1000 = cont = menor = 0
prod_barato = ' '
while True:
    prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    valor += preco
    continuar = ' '
    if preco > 1000:
        prod_mais1000 += 1
    cont += 1
    if cont == 1:
        menor = preco
        prod_barato = prod
    elif preco < menor:
        menor = preco
        prod_barato = prod
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${valor:.2f}')
print(f'Temos {prod_mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato} que custa {menor}')
