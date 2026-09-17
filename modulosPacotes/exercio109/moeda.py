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
