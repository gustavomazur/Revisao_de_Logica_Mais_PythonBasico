
lista = []
while True:
    print('Deseja Sair do programa [S/N]')
    opcao = str(input('Digite uma opcao: '))

    if opcao in 's':
        print('Saindo do programa...')
        break

    if opcao in 'n':

        numero = int(input('Digite um numero: '))
        lista.append(numero)
        print(f'Você digitou {len(lista) + 1} elementos.')
        lista.sort(reverse=True)
        print(f'Os valores em ordem descrescrente são {lista}')

        if 5 in lista:
            print('Valor 5 faz parte da lista! ')
        else:
            print('O valor 5 não foi encontrado na lista! ')



