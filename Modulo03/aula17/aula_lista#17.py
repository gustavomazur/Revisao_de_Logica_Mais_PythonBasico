def lin():
    print('-' * 30)

# Trocando as crases por aspas simples
lista = ['banana', 'sorvete']

del lista[0]

for item in lista:
    print(item)

lin()

# Vai de 2 até 44, pulando de 10 em 10 (gera: 2, 12, 22, 32, 42)
valores = list(range(2, 45, 10))
for item in valores:
    print(item)

lin()

# a lista numeros nao esta em ordem
# com sorte organiza
numeros = [8, 2, 5, 4, 9, 3, 0]
numeros.sort()
for para in numeros:
    print(para)

lin()

# para organizar na ordem reversa
numero = [8, 2, 5, 4, 9, 3, 0]
numero.sort(reverse=True)
for para in numero:
    print(para)

lin()

#len pra contar minha lista
print(len(numero))


