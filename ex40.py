valor = float(input('Qual valor você quer sacar? R$'))
cont_200 = 0
cont_100 = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_5 = 0
cont_2 = 0

somatorio = 0
debito_valor = valor - somatorio
while somatorio < valor:
    if somatorio + 200 > debito_valor:
        break
    else:
        somatorio += 200
        cont_200 += 1
while somatorio < valor:
    if somatorio + 100 > debito_valor:
        break
    else:
        somatorio += 100
        cont_100 += 1
while somatorio < valor:
    if somatorio + 50 > debito_valor:
        break
    else:
        somatorio += 50
        cont_50 += 1
while somatorio < valor:
    if somatorio + 20 > debito_valor:
        break
    else:
        somatorio += 20
        cont_20 += 1
while somatorio < valor:
    if somatorio + 10 > debito_valor:
        break
    else:
        somatorio += 10
        cont_10 += 1
while somatorio < valor:
    if somatorio + 5 > debito_valor:
        break
    else:
        somatorio += 5
        cont_5 += 1
while somatorio < valor:
    if somatorio + 2 > debito_valor:
        break
    else:
        somatorio += 2
        cont_2 += 1
if cont_200 > 0:
    print(f'Sacando {cont_200} cédulas de R$200')
if cont_100 > 0:
    print(f'Sacando {cont_100} cédulas de R$100')
if cont_50 > 0:
    print(f'Sacando {cont_50} cédulas de R$50')
if cont_20 > 0:
    print(f'Sacando {cont_20} cédulas de R$20')
if cont_10 > 0:
    print(f'Sacando {cont_10} cédulas de R$10')
if cont_5 > 0:
    print(f'Sacando {cont_5} cédulas de R$5')
if cont_2 > 0:
    print(f'Sacando {cont_2} cédulas de R$2')
print(f'Um total de R${somatorio:.2f}')
if valor > somatorio:
    print(f'Não foi possível sacar 1 real pois não realizamos saque de moedas')
