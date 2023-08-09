print('=' * 25)
print('10 TERMOS DE UMA PA')
print('=' * 25)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
t10 = t1 + razao * 10
for c in range(t1, t10, razao):
    print(c, end=' -> ')
print('ACABOU')