


def voto(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade < 16:
        return (f'Com {idade} anos: Não vota.')
    elif 16 <= idade <= 18 or idade >= 65:
        return (f'Com {idade} anos: Voto opcional.')
    else:
        return f'com {idade} anos: voto Obrigado.'

nascimento = int(input('Em quem ano você nasceu? '))
print(voto(nascimento))

