def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n:Vai receber uma ou mais notas (aceita várias).
    :param sit: situação parementro opcional
    :return: retorna a maior total de nota, maior, menor e a media das notas.
    :sit=False ou sit=True: se for False não aparece a situação se colocar True
    Aparece a situação explo linha 24 e 25
    :situacao: fala se a situação é boa, razoável ou RUIM
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#resp = notas(5.5, 2.5, 9, 8.5)
# resp = notas(5.5, 2.5, 9, 8.5 sit=True)
#print(resp)
help(notas)

