
num = [[], []]
for c in range(1, 8):
    val = int(input(f'Digite o {c}o valor: '))
    if val % 2 == 0:
        num[0].append(val)
    elif val % 2 == 1:
        num[1].append(val)
print('-' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
