def soma(a, b):
    resultado = a + b
    return resultado

def subtracao(a, b):
    resultado = a - b
    return resultado

def multiplicacao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    resultado = a / b
    return resultado

def lin():
    print('\033[0;32;40m-\033[m' * 30)

lin()
while True:
    print('Escolha uma opção:')
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Sair')

    opcao = int(input('Escolha uma opção: '))
    lin()

    if opcao == 5:
        print('\033[0;35;40mSair\033[m')
        break

    a = float(input('Informe o primeiro valor: '))
    lin()
    b = float(input('Informe o segundo valor: '))

    if opcao == 1:
        lin()
        print('Soma: {}'.format(soma(a, b)))
        lin()
    elif opcao == 2:
        lin()
        print('Subtrair: {}'.format(subtracao(a, b)))
        lin()
    elif opcao == 3:
        lin()
        print('\033[0;31;40mMultiplicar:\033[m {}'.format(multiplicacao(a, b)))
        lin()
    elif opcao == 4:
        lin()
        print('\033[0;33;40mDividir:\033[m {}'.format(divisao(a, b)))
        lin()
    else:
        print('Opção inválida!')
