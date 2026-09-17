def ficha(nome = '<Desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols')

nome = '<Desconhecido>'
gol = 0

nome = input('Digite o nome do jogador: ')
gol = input('Quantos gol: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(gol = gol)
else:
    ficha(nome = gol)


