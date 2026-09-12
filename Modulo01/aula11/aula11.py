print('\033[0;30;41mTeste\033[m')
print('\033[4;33;46mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')
print('\033[1;31;43mOlá mundo\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[33m{}\033[m'.format(a,b))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m'}
nome = 'Lorena'
nome1 = 'Gustavo'

print('Olá Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome,'\033[m'))

print('Hi My {}{}{}, How are you?'.format(cores['azul'], nome1, cores['limpa']))