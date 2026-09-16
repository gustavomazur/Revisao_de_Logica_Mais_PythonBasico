from operator import itemgetter
from random import randint
from time import sleep

dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6),}
#ranking = dict()
list = list()
print('Valores sorteados:')
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado. ')
    sleep(1)
#rankig = sorted(dados.items(), key=itemgetter(1), reverse=True)
list = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('Ranking dos jogadores: ')
#for i, (jogador, v) in enumerate(list, start=1):
 #   print(f'{i}⁰ lugar: {jogador} com {v}.')
  #  sleep(1)
for i, v in enumerate(list):
    print(f'{i}⁰ lugar: {v[0]} com {v[1]}.')
    sleep(1)

#key=lambda ordena usando o valor o item[1]
#O item: é a tupla inteira -> jogador1 + 3 = key + V
#itemetter(1) Mostra em ordem de valor
#itemetter(0) Mostra em ordem de chave

