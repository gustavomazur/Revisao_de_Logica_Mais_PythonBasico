def leiaInt(numero):
    ok = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31;40mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero inteiro: ')
print(f'O valor digitado foi {n} e interio ')

