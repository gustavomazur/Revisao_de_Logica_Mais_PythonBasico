from random import shuffle

nome = str(input('Digite o nome do primeiro aluno: '))
nome1 = str(input('Digite o nome do segundo aluno: '))
nome2 = str(input('Digite o nome do terceiro aluno: '))
nome3 = str(input('Digite o nome do quarto aluno: '))

lista = [nome, nome1, nome2, nome3]
shuffle(lista)
print(lista)

