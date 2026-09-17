#Indentificado por {} Chaves
dado = dict()
#Pedro é valor é nome é indentifcador do valor
dados = {'nome':'Pedro','idade':25}
print(dados['nome'])#Pedro
print(dados['idade'])#25
#Adicionar valor no Dicionario
dados['sexo']= 'M'
#Remover Valor do Dicionario
del dados['idade']

print('-=' * 30)

filme = {'titulo':'Star Wars',
         'ano':1999,
         'diretor':'George Lucas'
}
#Vai imprimir todos os dados do meu Dicionario
print(filme.values())
# Se eu quiser pegar as Chaves que são
# Titulo, Ano, Diretor, Eu uso
print(filme.keys())
#se eu quiser tanto o valor é chave, Eu uso
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')

#Test
pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade':23}
pessoas ['nome'] = 'Lorena'
pessoas['kg'] = 80
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos, sexo {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


#Posso colocar um Dicionario dentro de uma lista
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'são Paulo', 'sigle': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#na lista usamos [:]
#No Dicionario usamos copy()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
    for k, v in e.item():
        print(f'O campo {k} tem valor {v}')