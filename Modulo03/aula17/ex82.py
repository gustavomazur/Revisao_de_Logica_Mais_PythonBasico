
lista = []
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = (input('Quer continuar? [S/N]'))

    if resposta in 'Nn':
        print('Finalizando...')
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('-' * 30)
print(f'A lista completa {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')
