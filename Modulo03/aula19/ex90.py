ficha = {
    'Nome': '',
    'Média': '',
}
ficha['Nome'] = str(input('Nome: '))
ficha['Média']= float(input('Média: '))
if ficha["Média"] >= 6:
    print(f'Nome: {ficha["Nome"]}')
    print(f'Média é igual a {ficha["Média"]}')
    print('Situação é igual a Aprovado')
else:
    print(f'Nome: {ficha["Nome"]}')
    print(f'Média é igual a {ficha["Média"]}')
    print('Situação é igual a reprovado')