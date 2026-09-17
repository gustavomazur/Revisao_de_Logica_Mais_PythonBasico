from exercio108.moeda import metade, dobro, aumentar, diminuir, moeda

p = float(input('Digite o preço R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
print(f'Menos 10% {moeda(diminuir(p, 10))}')
