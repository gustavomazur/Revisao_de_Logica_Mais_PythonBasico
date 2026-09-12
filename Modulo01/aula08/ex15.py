#import math
#from math import sqrt
from math import sqrt, floor
num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, raiz)) -> mostra a raiz quadrada
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #-> Redonda para cima
#print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))