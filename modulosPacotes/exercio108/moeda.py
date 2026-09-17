def aumentar(p=0, t=0):
    resp = p + (p * t / 100)
    return resp
def diminuir(p=0,  t=0):
    resp = p - (p * t / 100)
    return resp

def dobro(p=0):
    resp = p * 2
    return resp

def metade(p=0):
    resp = p / 2
    return resp

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:8.2f}'.replace('.', ',')