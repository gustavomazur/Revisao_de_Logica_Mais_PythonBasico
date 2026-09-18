def aumentar(p=0, t=0, formato = False):
    resp = p + (p * t / 100)
    return resp if formato is False else moeda(resp)
def diminuir(p=0,  t=0, formato = False):
    resp = p - (p * t / 100)
    return resp if formato is False else moeda(resp)

def dobro(p=0, formato = False):
    resp = p * 2
    return resp if formato is False else moeda(resp)

def metade(p=0, formato = False):
    resp = p / 2
    return resp if formato is False else moeda(resp)

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:8.2f}'.replace('.', ',')

def resumo(p=0, t=10, txd=15,):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{txd}% de aumento: \t{aumentar(p, txd, True)}')
    print(f'{t}% de redução: \t{diminuir(p, t, True)},')
    print('-' * 30)


