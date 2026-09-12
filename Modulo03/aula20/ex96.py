def area(largura, comprimento):
    a = largura * comprimento
    print('-' * 30)
    print(f'Seu terreno tem \033[0;32;40m{a}m²\033[m')

largura = float(input('Qual a largura do terreno ?'))
comprimento = float(input('Qual o comprimento do terreno ?'))

area(largura, comprimento)
