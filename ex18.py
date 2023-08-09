peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O seu imc é de {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso normal')

elif 18.5 <= imc < 25:
    print('Você está na faixa de peso normal')

elif 25 <= imc < 30:
    print('Você está em sobrepeso')

elif 30 <= imc < 40:
    print('Você está na faixa de obesidade')

else:
    print('Você está na faixa de obesidade mórbida')
