print('informe numero de 3 retas para ver se forma um triângulo: ')
n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('seus valores formam um triângulo')
else:
    print('seus valores não formam um triângulo')
