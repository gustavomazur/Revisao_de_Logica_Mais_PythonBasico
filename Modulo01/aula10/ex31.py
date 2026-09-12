print('Passagem'.center(28))
print('acima de 200km ganha desconto: ')
print('-'*30)

d = float(input('Qual é a distância da sua viagem? '))

if d <= 200:
    valor = d * 0.50
    print('o Valor da sua passagem R${}'.format(valor))
else:
    valor = d * 0.45
    print('o Valor da sua passagem R${}'.format(valor))
