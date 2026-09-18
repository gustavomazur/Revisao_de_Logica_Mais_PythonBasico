from exercio112.utilidades import moeda
from exercio112.utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$')
"""
p -> Preço
20 -> redução
12 -> Aumento
"""
moeda.resumo(p, 12, 20)

