from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
qnts = int(input('Quantos jogos deseja gerar: '))
tot = 1
while tot <= qnts:
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-=' * 3, f' SORTEANDO {qnts} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, f'BOA SORTE!', '-=' * 5)