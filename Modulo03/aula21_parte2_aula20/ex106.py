
from time import sleep


#Lista Cores Global
cores = ('\033[m',               #0 - Sem cores
         '\033[0;30;41m',        #1 - vermelho
         '\033[0;30;42m',        #2 - verde
         '\033[0;30;43m',        #3 - amarelo
         '\033[0;30;44m',        #4 - azul
         '\033[0;30;45m',        #5 - roxo
         '\033[0;30;47m',           #6 - branco
 );

#Função principal que vai receber o comando que eu quero execultar
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)

#Titulo pra mostrar as linhas personalisadas
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)