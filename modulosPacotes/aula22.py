from uteis import numeros

#simplificação
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')


"""
Organização do código
Facilidade na manuntenção
Ocultação de código detalhado
Reutlização em outros projetos
se ficar muito grande solução usar pacotes
vai separar varios modulos cada modulo pra uma coisa espesifica
cada pasta é um pacote é dentro dessa pasta vai conter varios modulos
ou criar outra pasta que é pacote é criar os modulos lá 
"""