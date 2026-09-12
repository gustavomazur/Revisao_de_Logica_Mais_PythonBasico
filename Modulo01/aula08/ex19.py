from random import choice

nome = str(input('Digite primeiro nome do aluno: '))
nome1 = str(input('Digite segundo nome do aluno: '))
nome2 = str(input('Digite terceiro nome do aluno: '))
nome3 = str(input('Digite quarto nome do aluno: '))
lista = [nome, nome1, nome2, nome3]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

