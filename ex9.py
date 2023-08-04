sexo = ''
idade = 0
qtdMulheres = 0
qtdHomens = 0

for i in range(0,5):
    sexo = input('Digite o sexo (M ou H): ')
    idade = int(input('Digite a idade: '))

    if (sexo =='M' or sexo =='m'):
        qtdMulheres+=1
    elif (sexo =='H' or sexo =='h'):
        qtdHomens+=1

print('A quantidade de mulheres é', qtdMulheres)
print('A quantidade de homens é', qtdHomens)
