
from datetime import datetime

dicionario = dict()
dicionario['nome'] = str(input('nome: '))
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = datetime.now().year - nascimento
dicionario['ctps'] = int(input('Tem carteira de trabalho? (0 não tem):'))
if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('salário: R$ '))
    dicionario['aposentadria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dicionario.items():
    print(f' - {k} tem o valor {v}')

