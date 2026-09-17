from exercio109.moeda import metade, dobro, aumentar, diminuir, moeda

p = float(input('Digite o preço R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Menos 10% {diminuir(p, 10, True)}')
