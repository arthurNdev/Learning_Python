listaNomes = []

while True:
    nome = input('Digite um nome: ')
    listaNomes.append(nome)

    continuar = input('Deseja continuar? Digite sim ou não: ')
    if(continuar == 'não' or continuar == 'nao'):
        break

print(listaNomes)