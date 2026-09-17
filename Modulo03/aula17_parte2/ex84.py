lista = list()
pessoas = list()
leve = list()
pesado = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    pessoas.append(lista[:])
    lista.clear()
    if str(input('Quer continuar? [S/N')) in 'Nn':
        break

print(pessoas)

for p in pessoas:
    if p[1] >= 75:
        pesado.append(p)
    else:
        leve.append(p)

print(f'As pessoas mais leve são {leve}')
print(f'As pessoas mais pesada são {pesado}')






