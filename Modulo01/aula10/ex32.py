from calendar import isleap
from datetime import date

n = int(input('Digite o ano para saber se é bissexto ou não / Digite 0 para verificar o ano atual: '))

if n == 0:
    n = date.today().year
r = isleap(n)
if r == True:
    print('{} é Bissexto!'.format(n))
else:
    print('{} não é bissexto!'.format(n))
