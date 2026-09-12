import time
lista = []
def lin():
    print('-' * 30)

while True:

    print('Escolha uma opção:')
    print('Deseja sair? [s/n]')
    opcao = str(input('Digite a opção escolhida: '))
    if opcao == 's':
        print('\033[0;31;40msaindo', end=' ')
        for cada in range(3):
            print('.', end=' ', flush=True)
            time.sleep(1)
        print('\033[m')
        break
    if opcao == 'n':
        print('\033[0;32;40mContinuar...\033[m')

        valor = input('Digite um valor: ')

        if valor in lista:
            lin()
            print('Valor duplicado! não vou adicionar...')
            lin()
            continue
        lista.append(valor)

        for cada in range(3):
            print('.', end = ' ', flush = True)
            time.sleep(1)
        lista.sort()
        print(f'Você digitou os valores {lista}')
        print('-' * 30)
