#Lista compostas
#Elemento 0,1
#dados = ['Pedro', 25]

#pessoas = list()
                #Pessoas

#         0    |       1    |      2
#|--------------------------------------|
#|  Pedro | 25 | Maria | 19 | João | 32 |
#|    0   |  1 |   0   |  1 |   0  | 1  |
#|--------------------------------------|
#elemento1
#[Pedro,25]
#pessoas.append(dados[:])

#primeiro [] -> chama qual estrutura [] -> segundo chama objt
#print(pessoas[0][1])
#print(pessoas[1])# Quero tudo
#print(pessoas[0][0])#Pedro
#print(pessoas[1][1])#19
#print(pessoas[2][2])#João
#print(pessoas[1]) #Maria, 19
#------------Pratica---------------------
def lin():
    print('-' * 30)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[1][1])
lin()
#Mostra todos os nome é idade
for i in galera:
    print(i)
lin()
#Mostra todas idades
for i in galera:
    print(i[1])
lin()
#Mostra todos os nomes
for i in galera:
    print(i[0])
lin()

#Formatando
for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade')
lin()
#Adicionando
pessoas = list()
informacao = list()

for i in range(0, 5):
    informacao.append(str(input('Digite seu nome: ')))
    informacao.append(int(input('Digite sua idade: ')))
    pessoas.append(informacao[:])
    informacao.clear()

print(pessoas)

lin()
totmai = totmen = 0
for p in pessoas:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]}é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
