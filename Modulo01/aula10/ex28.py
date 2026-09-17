from random import randint
from time import sleep

aletorio = randint(0, 5)

print('---' * 15)
print('Tente adivinhar o numero aletorio entre 0 e 5')
print('---' * 15)

n = int(input('Digite algum numero de 0 á 5 : '))

print('Processando...')
sleep(2)

if n == aletorio:
    print('Você venceu')
else:
    print('Você perdeu')
