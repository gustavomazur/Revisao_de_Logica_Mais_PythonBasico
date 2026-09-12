def linha():
    print('-'*30)
menor = 0
maior = 0
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
linha()
print(f'você digitou os valores {lista} ')
print(f'O Maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
      print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()
