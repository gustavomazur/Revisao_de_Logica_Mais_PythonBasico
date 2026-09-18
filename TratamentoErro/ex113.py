def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print('\033[0;31;40mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31;40m Usúario preferiu sair. \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite valor valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31;40m Usúario preferiu sair. \033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
