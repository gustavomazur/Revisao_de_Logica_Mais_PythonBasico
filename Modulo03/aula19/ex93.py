jogador = dict()
partidas = list()
def linha():
    print('-=' * 30)
jogador['nome'] = str(input('Nome do jogar: '))
tot = int(input(f'Qunatas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
linha()
print(jogador)
linha()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
linha()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols. ')
