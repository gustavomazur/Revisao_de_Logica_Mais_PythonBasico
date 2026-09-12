print("""Digite 3 numeros inteiros:
para saber qual é o maior numero
é o menor numero: """)

n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo  numero: '))
n3 = int(input('Digite terceiro numero: '))
#Verifica quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verifica quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O Menor valor digitado foi {}'.format(menor))
print('O Maior valor digitado foi {}'.format(maior))

'''Oque eu fiz
if n1 > n2 and n1 > n3:
    print('maior numero{}'.format(n1))
    if n2 < n3:
        print('menor numero {}'.format(n2))
    else:
        print('menor numero {}'.format(n3))
elif n2 > n1 and n2 > n3:
    print('maior numero {}'.format(n2))
    if n3 < n1:
        print('menor numero {}'.format(n3))
    else:
        print('menor numero {}'.format(n1))
elif n3 > n1 and n3 > n2:
    print('maior numero {}'.format(n3))
    if n1 < n2:
        print('menor numero {}'.format(n1))
    else:
        print('menor numero {}'.format(n2))'''

